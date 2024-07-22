#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL username, password, and database name from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Create an engine connected to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{db_name}', pool_pre_ping=True)
    
    # Create all tables in the database (if they don't exist)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create a new State object for Louisiana
    new_state = State(name="Louisiana")

    # Add the new state to the session
    session.add(new_state)

    # Commit the session to the database
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close the session
    session.close()