from mysql.connector import Error

from dml.connection_pool import ConnectionPool


def insert_product(sql, code, name):  # 한 행 삽입
    args = (code, name)
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def insert_products(sql, products):  # 여러 행
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.executemany(sql, products)
        conn.commit()
    except Error as e:
        print('Error:', e)
    finally:
        cursor.close()
        conn.close()
