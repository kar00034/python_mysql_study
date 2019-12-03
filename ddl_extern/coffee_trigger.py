# from mysql.connector import errorcode, Error
# from connection_pool.connection_pool_study02 import ExplicitlyConnectionPool
# from ddl.mysql_ddl_sql import DB_NAME
#
# trigger = {'': (
#     """""")
# }
#
#
# def create_trigger():
#     try:
#         conn = ExplicitlyConnectionPool.get_instance().get_connection()
#         cursor = conn.cursor()
#         cursor.execute("USE {}".format(DB_NAME))
#         for trigger_name in trigger:
#             trigger_description = trigger[trigger_name]
#             print('trigger_description', trigger_description)
#             try:
#                 cursor.execute("drop trigger {}".format(trigger.keys()))
#                 print("drop trigger {}".format(trigger.keys()))
#             except err.errno == errorcode.ER_NO_TRIGGERS_ON_SYSTEM_SCHEMA:
#                     print("already drop trigger")
#             else: Error as err:
#                 print(err.msg)
#             finally:
#                 cursor.execute("{}".format(trigger.values()))
#                 print("Creating trigger\ndelimiter $$\n {}\ndelimiter ;".format(trigger_name), end='')
#                 cursor.execute(trigger_description)
#     except Error as err:
#         print(err)
#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()
