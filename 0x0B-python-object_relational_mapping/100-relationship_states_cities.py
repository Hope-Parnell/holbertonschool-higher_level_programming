#!/usr/bin/python3
"""creates a state and a city"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    sf = City(name="San Francisco")
    cali = State(name="California")
    cali.cities.append(sf)
    session.add_all([cali, sf])
    session.commit()
    session.close()
