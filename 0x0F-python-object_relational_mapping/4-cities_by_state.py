#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    host_name = "localhost"
    port_name = 3306
    user_name = argv[1]
    passwd = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host=host_name, port=port_name, user=user_name,
                         passwd=passwd, db=database)

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities, states\
    WHERE cities.state_id=states.id ORDER BY cities.id")

    rows = cur.fetchall()
    for city in rows:
        print(city)

    cur.close()
    db.close()
