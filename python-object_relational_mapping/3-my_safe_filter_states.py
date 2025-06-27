#!/usr/bin/python3
"""
    script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument (safe from SQL injection)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = db.cursor()
    # Use parameterized query to avoid SQL injection
    cursor.execute(
        "SELECT * FROM states WHERE name = BINARY %s ORDER BY id ASC",
        (sys.argv[4],)
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
