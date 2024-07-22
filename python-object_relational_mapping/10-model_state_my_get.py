#!/usr/bin/python3
"""
lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                    argv[1], argv[2], argv[3], pool_pre_ping=True))

    state_name = argv[4]

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == state_name).first()
    if states is not None:
        print('{}'.format(states.id))

    if states is None:
        print("Not found")

    session.close()