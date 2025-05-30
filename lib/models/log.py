from sqlalchemy import Integer, Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from lib.models import Base
from datetime import datetime

class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.now)
    status = Column(String)
    habit_id = Column(Integer, ForeignKey('habits.id'))

    habit = relationship("Habit", back_populates="logs")

    @classmethod
    def get_logs_by_habit(cls, session, habit_name):
        return session.query(cls).filter_by(habit_name=habit_name).order_by(cls.timestamp).all()
    

    def __repr__(self):
        return f"<Log id={self.id} habit_id={self.habit_id} status='{self.status}'"