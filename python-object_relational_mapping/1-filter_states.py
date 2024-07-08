import MySQLdb
import sys


def list_states_with_N(username, password, database):
    try:
        # Conectarse a la base de datos
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
        )
        cursor = db.cursor()

        # Consulta para obtener los estados que comienzan con 'N'
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)

        # Obtener los resultados
        results = cursor.fetchall()

        # Mostrar los resultados
        for row in results:
            print(row)

        # Cerrar la conexión
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states_with_N(username, password, database)
