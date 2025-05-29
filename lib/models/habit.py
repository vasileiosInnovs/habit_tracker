from sqlalchemy import Column, Integer, String
from lib.models import Base
from sqlalchemy.orm import relationship

class Habit(Base):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    time_period = Column(String)
    category = Column(String)
    frequency = Column(Integer)

    logs = relationship("Log", back_populates="habit", cascade="all, delete-orphan")

    def __repr__(self):
        return (
            f"<Habit Id=(id={self.id}, Name='{self.name}', Description='{self.description}', "
            f"Time Period='{self.time_period}, Category='{self.category}, Frequency={self.frequency}')>"
            )

    def save(self, session):
        session.add(self)
        session.commit()

    