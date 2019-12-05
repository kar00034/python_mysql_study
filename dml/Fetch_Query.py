from dml.connection_pool import ConnectionPool
from mysql.connector import Error

def iter_row(cursor,size=5):
    while True:
        rows=cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


def qurey_with_fetchmany(sql):
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        for row in iter_row(cursor,5):
            print(type(row)," ",row)
    except Error as e:
        print(e)
    finally:
        cursor.cloes()
        conn.close()