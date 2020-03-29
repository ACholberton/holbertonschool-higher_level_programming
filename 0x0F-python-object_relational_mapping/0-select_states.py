#!/usr/bin/python3
"""
this script lists all the states from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    host = "localhost"
    port = 3306
    user = argv[1]
    passwd = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host=host, port=port, user=user,
                               passwd=passwd, db=database)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id;")
    rows = cur.fetchall()
    for state in rows:
        print(states)

    cur.close()
    db.close()
