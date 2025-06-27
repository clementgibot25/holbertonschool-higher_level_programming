#!/usr/bin/python3
"""
Script that lists all cities of a specific state from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connection to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Get the state name to search for
    state_name = sys.argv[4]

    # Create a cursor object
    cur = db.cursor()

    # Execute the query with parameterized input
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    # Fetch all the rows
    cities = cur.fetchall()

    # Print the city names separated by commas
    print(", ".join(city[0] for city in cities))

    # Close cursor and database connection
    cur.close()
    db.close()
