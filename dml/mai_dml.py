#!/usr/bin/env python
from dml.coffee_select import query_with_fetchall, query_with_fetchone, query_with_fetchall_by_code


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
    # sql_test()
    # fetchone_test()
    # fetchall_test()
    res = query_with_fetchall_by_code(sql, 'A001')
    print(res)
    # query_with_fetchall_by_code(sale)
