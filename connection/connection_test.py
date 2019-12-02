from mysql.connector import MySQLConnection

try:
    conn = MySQLConnection(host="localhost",
                           database="mysql",
                           user="root",
                           password="rootroot")

    print(conn)
except AttributeError as error:
    print(error)
