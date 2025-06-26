#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )
    
    # Create a cursor object
    cur = db.cursor()
    
    # Execute the SQL query
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all rows
    rows = cur.fetchall()
    
    # Print each row
    for row in rows:
        print(row)
    
    # Close cursor and database connection
    cur.close()
    db.close()
