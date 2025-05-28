import datetime
from sqlalchemy import UniqueConstraint, Column, Integer, String, DateTime
from lib.models import Base

class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        UniqueConstraint(
            'email', 
            name = 'unique_email'
        ),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(55))
    signup_date = Column(DateTime(), default=datetime.datetime.now)

    def __repr__(self):
        return f"<User(id={self.id}, Name='{self.name}', Email Address='{self.email}', Sign Up Date='{self.signup_date}')>"