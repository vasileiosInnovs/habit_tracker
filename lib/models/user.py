import datetime
from sqlalchemy import UniqueConstraint, Column, Integer, String, DateTime
from lib.models import Base
import re
from sqlalchemy.orm import Session

class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        UniqueConstraint(
            'email', 
            name = 'unique_email'
        ),
    )

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    _email = Column("email", String(55))
    signup_date = Column(DateTime(), default=datetime.datetime.now)
    password = Column(String, nullable=False)

    def __init__(self, email=None):
        self._email = email

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            raise ValueError('Invalid email address')
        self._email = email

    def __repr__(self):
        return f"<User(id={self.id}, Name='{self.username}', Email Address='{self.email}', Sign Up Date='{self.signup_date}')>"
    
    def update(self, session: Session, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        session.commit()

    def delete(self, session: Session):
        session.delete(self)
        session.commit()

    @classmethod
    def create(cls, session: Session, **kwargs):
        habit = cls(**kwargs)
        session.add(habit)
        session.commit()
        return habit
    
    @classmethod
    def get_by_username(cls, session: Session, username):
        return session.query(cls).filter_by(username=username).first()