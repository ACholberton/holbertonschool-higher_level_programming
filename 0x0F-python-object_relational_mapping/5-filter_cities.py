#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities
 of that state, using the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    host_name = "localhost"
    port_name = 3306
    user_name = argv[1]
    passwd = argv[2]
    database = argv[3]
    sname = argv[4]

    db = MySQLdb.connect(host=host_name, port=port_name, user=user_name,
                         passwd=passwd, db=database)

    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities, states WHERE state_id =\
    states.id AND states.name = %s ORDER BY cities.id", (sname, ))

    rows = cur.fetchall()
    print(', '.join(city[0] for city in rows))

    cur.close()
    db.close()
