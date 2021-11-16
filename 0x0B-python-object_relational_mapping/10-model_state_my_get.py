#!/usr/bin/python3
"""Finds States that contain 'a' using SQLAlchemy"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    found = False
    for state in session.query(State).filter(State.name == argv[4]):
        print(state.id)
        found = True
    if not found:
        print("Not found")
