from dml.connection_pool import ConnectionPool
from mysql.connector import Error, errorcode

procedure_name = 'proc_sale_stat'
procedure_src = """
    create procedure proc_sale_stat()
    begin
        select sum(@saleprice:=price*salecnt) sale_price,
               sum(@addtax:=ceil(@saleprice/11)) addtax_price,
               sum(@supprice:=@saleprice - @addtax) supply_price,
               sum(@marPirce:=round(@supprice * (marginrate/100))) margin_price
        from sale s join product p on s.code = p.code;
    END
"""


def create_procedure():
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(procedure_src)
        print("create procedure {}".format(procedure_name))
    except Error as err:
        if err.errno == errorcode.ER_SP_ALREADY_EXISTS:
            cursor.execute("drop procedure {}".format(procedure_name))
            print("drop procedure {}".format(procedure_name))
            cursor.execute(procedure_src)
            print("create procedure {}".format(procedure_name))
        else:
            print(err.msg)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def call_sale_stat_sp(query):
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.callproc(query)
        for result in cursor.stored_results():
            res = result.fetchone()
            print(res)
    except Error as err:
        print(err)
    finally:
        cursor.close()
        conn.close()


def call_order_price_by_issale(query, isSale):
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()

        args = [isSale, ]
        cursor.callproc(query, args)
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                print(row)
    except Error as err:
        print(err)

    finally:
        cursor.close()
        conn.close()
