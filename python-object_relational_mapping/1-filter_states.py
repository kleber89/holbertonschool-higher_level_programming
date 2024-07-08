import MySQLdb
import sys


def get_states_by_name_pattern(username, password, database):
    """
    This function retrieves all states with a name starting with 'N' from a MySQL database.

    Args:
        username: Username to connect to the MySQL database.
        password: Password to connect to the MySQL database.
        database: Database name to query.
    """

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"

    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
