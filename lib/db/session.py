from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models.base import Base

from lib.models.user import User
from lib.models.habit import Habit
from lib.models.log import Log

engine = create_engine('sqlite:///better_everyday.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()