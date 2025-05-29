from sqlalchemy import Column, Integer, String, ForeignKey
from lib.models import Base
from sqlalchemy.orm import relationship

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