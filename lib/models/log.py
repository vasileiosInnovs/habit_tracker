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

    def __repr__(self):
        return f"<Log id={self.id} habit_id={self.habit_id} status='{self.status}'"