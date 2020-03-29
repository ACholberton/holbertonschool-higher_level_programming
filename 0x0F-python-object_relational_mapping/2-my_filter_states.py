#!/usr/bin/python3
"""
this script takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
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

    cur.execute("SELECT * FROM states WHERE BINARY name = '{}' \
    ORDER BY id; ".format(sname))
    rows = cur.fetchall()
    for states in rows:
        print(states)

    cur.close()
    db.close()
