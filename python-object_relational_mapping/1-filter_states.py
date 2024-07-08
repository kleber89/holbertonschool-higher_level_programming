import sys
import MySQLdb


def main(username, password, database):
    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost", port=3306, user=username, passwd=password, db=database
        )
        cursor = db.cursor()

        # Execute query
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)

        # Fetch all rows
        results = cursor.fetchall()

        # Display results
        for row in results:
            print(row)

        # Commit the transaction
        db.commit()

        # Close cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    main(username, password, database)
