#!/usr/bin/python3
"""
this script lists all the states from the database hbtn_0e_0_usa
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

    cur.execute("SELECT * FROM states ORDER BY states.id;")
    rows = cur.fetchall()
    for states in rows:
        print(states)

    cur.close()
    db.close()
