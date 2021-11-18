#!/usr/bin/python3
"""Module contains the city class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """class for cites in database"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
