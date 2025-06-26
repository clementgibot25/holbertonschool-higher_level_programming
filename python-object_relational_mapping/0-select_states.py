#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""

if __name__ == "__main__":
   from sys import argv
   import MySQLdb

   db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
   cur = db.cursor()
   cur.execute("SELECT * FROM states ORDER BY id ASC")
   rows = cur.fetchall()
   for row in rows:
       print(row)
   cur.close()
   db.close()
