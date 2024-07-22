#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset='utf8')
    cur = db.cursor()

    sql = "SELECT cities.name\
            FROM states\
            INNER JOIN cities ON states.id  = cities.state_id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC"

    cur.execute(sql, (argv[4],))
    print(", ".join([city[0] for city in cur.fetchall()]))

    cur.close()
    db.close()