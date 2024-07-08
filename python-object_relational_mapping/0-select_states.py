#!/usr/bin/python3
"""
list_states.py: Script that lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


def list_states():
    """
    Connect to MySQL database and list all states sorted by states.id.
    """
    # Database connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cur = db.cursor()

    # Execute query
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch and display results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
