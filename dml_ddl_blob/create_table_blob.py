from dml.connection_pool import ConnectionPool
from mysql.connector import Error,errorcode

table_name = 'images'
table_sql = """
create table images(
    no int primary key auto_increment,
    name varchar(20) not null,
    pic longblob not null
)
"""


def create_table():
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(table_sql)
        print("create table {}".format(table_name))
    except Error as err:
        print(err)
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            cursor.execute("DROP TABLE {}".format(table_name))
            print("drop table {}".format(table_name))
            cursor.execute(table_sql)
            print("create table {}".format(table_name))
        else:
            print(err.msg)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()