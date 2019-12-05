from mysql.connector import Error

from dml.connection_pool import ConnectionPool


def update_products(sql, name, code):
    args = (name, code)
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()
    except Error as err:
        print(err)
    finally:
        cursor.close()
        conn.close()
