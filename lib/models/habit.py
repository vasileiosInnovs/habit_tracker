import datetime
from sqlalchemy import Column, Integer, String
from lib.models import Base

class Habit(Base):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    time_period = Column(String)
    category = Column(String)
    frequency = Column(Integer)

    def __repr__(self):
        return f"<User(id={self.id}, Name='{self.name}', Email Address='{self.email}', Sign Up Date='{self.signup_date}')>"