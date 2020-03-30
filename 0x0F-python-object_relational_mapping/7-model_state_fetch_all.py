#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""


import MySQLdb
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import State
from model_state import Base

if __name__ == "__main__":
    host_name = "localhost"
    port_name = 3306
    user_name = argv[1]
    passwd = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(state).order_by(State.id).all():
        print("{}: {}".format(instance.id, instance.name))

    session.close()
