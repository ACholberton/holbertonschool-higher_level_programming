#!/usr/bin/python3
"""
script that changes the name of a State object from the database
"""


import MySQLdb
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import State
from model_state import Base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).filter(State.id == 2).first()
    instance.name = "New Mexico"
    session.commit()

    session.close()
