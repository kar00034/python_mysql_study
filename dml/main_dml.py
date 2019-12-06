#!/usr/bin/env python
import pandas as pd

from dml.coffee_delete import delete_product
from dml.coffee_insert import insert_product, insert_products
from dml.coffee_select import query_with_fetchall, query_with_fetchone, query_with_fetchall_by_code
from dml.coffee_update import update_products
from dml.create_procedure import create_procedure, call_sale_stat_sp, call_order_price_by_issale
from dml.transaction_query import transaction_fail1, transaction_fail2, transaction_success


def sql_test():
    global product, sale
    product = "select * from product"
    sale = "select * from sale"


def fetchone_test():
    query_with_fetchone(product)
    query_with_fetchone(sale)


def fetchall_test():
    query_with_fetchall(product)
    query_with_fetchall(sale)


if __name__ == "__main__":
    sql = "select * from product where code = %s"
    sql_sel = "select * from product"
    sql_ins = "insert into product values (%s,%s)"
    ## select문
    # sql_test()
    # fetchone_test()
    # fetchall_test()
    # res = query_with_fetchall_by_code(sql, 'A001')
    # print(res)
    # query_with_fetchall_by_code(sale)
    # query_with_fetchall(sql_sel)
    # query_with_fetchall(sql_sel)

    ## insert
    # insert_product(sql_ins, 'C001', '라떼')
    # products = [('C002', '라떼2'), ('C003', '라떼3'), ('C004', '라떼4')]
    # insert_products(sql_ins, products)

    ## update
    # sql_up = "update product set name = %s where code = %s"
    # query_with_fetchall(sql_sel)
    # sel_up = query_with_fetchall_by_code(sql, 'C001')
    # print(sel_up)
    # update_products(sql_up, '라떼', 'C001')
    # sel_up = query_with_fetchall_by_code(sql, 'C001')
    # print(sel_up)
    # query_with_fetchall(sql_sel)

    ## delete
    # select_sql = "select code, name from product where like 'C__'"
    # res = query_with_fetchall(select_sql)
    #
    # columns_list = ['code', 'name']
    # df = pd.DataFrame(res, columns=columns_list)
    # print(df)
    #
    # sql_del = "delete from product where code = %s"
    # delete_product(sql_del, 'C004')
    #
    # query_with_fetchall(sql_sel)

    ##transaction
    # transaction_fail1()
    # transaction_fail2()
    # transaction_success()

    ## procedure
    # create_procedure()
    # call_sale_stat_sp('proc_sale_stat')
    # print()
    call_order_price_by_issale('proc_saledetail_orderby', False)
    print()
    call_order_price_by_issale('proc_saledetail_orderby', True)
