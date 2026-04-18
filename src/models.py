from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    schedule = Column(String)
    max_participants = Column(Integer)
    participants = relationship('Participant', back_populates='activity', cascade='all, delete-orphan')

class Participant(Base):
    __tablename__ = 'participants'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    activity_id = Column(Integer, ForeignKey('activities.id'))
    activity = relationship('Activity', back_populates='participants')
