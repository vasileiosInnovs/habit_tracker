from tabulate import tabulate
from sqlalchemy import Column, Integer, String, ForeignKey
from lib.models import Base
from sqlalchemy.orm import relationship
#from lib.models.log import Log

class Habit(Base):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    time_period = Column(String)
    category = Column(String)
    frequency = Column(Integer)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="habits")
    logs = relationship("Log", back_populates="habit", cascade="all, delete-orphan")

    def __repr__(self):
        return (
            f"<Habit Id=(id={self.id}, Name='{self.name}', Description='{self.description}', "
            f"Time Period='{self.time_period}, Category='{self.category}, Frequency={self.frequency}')>"
            )

    def save(self, session):
        session.add(self)
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()

    @classmethod
    def get_by_name(cls, session, name):
        return session.query(cls).filter_by(name=name).first()
    
    def view_report(self, session):
        from lib.models.log import Log
        
        logs = session.query(Log).filter_by(habit_id=self.id).order_by(Log.timestamp).all()

        if not logs:
            print("⚠️ No logs found.")
            return
        
        table = [[log.id, log.habit_name, log.status, log.timestamp.strftime("%Y-%m-%d %H:%M")] for log in logs]
        print(tabulate(table, headers=['ID', 'Habit', 'Status', 'Timestamp'], tablefmt="fancy_grid"))