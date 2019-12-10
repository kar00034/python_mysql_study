from dml.connection_pool import ConnectionPool
from mysql.connector import Error
from dml_ddl_blob.blob_read_write import read_file_blob, write_file_blob


def insert_blob(query,file_name,file_path):
    data = read_file_blob(file_path)
    args = (file_name, data)
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as err:
        print(err)
    finally:
        cursor.close()
        conn.close()


def update_blob(query,file_name,file_path,no):
    data = read_file_blob(file_path)
    args = (file_name, data, no)
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as err:
        print(err)
    finally:
        cursor.close()
        conn.close()


def read_blob(query, no, file_name):
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(query,(no,))
        photo = cursor.fetchone()[0]
        write_file_blob(photo, file_name)
    except Error as err:
        print(err)
    finally:
        cursor.close()
        conn.close()


def delete_blob(sql, no):
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql,(no,))
        conn.commit()
    except Error as err:
        print(err)
    finally:
        cursor.close()
        conn.close()