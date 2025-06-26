#!/usr/bin/python3
"""script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
"""Lists all states where name matches the argument."""

import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db
    )
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(name)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
