from dml.coffee_select import query_with_fetchall
from dml_ddl_blob.blob_read_write import read_file_blob
from dml_ddl_blob.blobl_query import insert_blob, read_blob, update_blob, delete_blob
from dml_ddl_blob.create_table_blob import create_table

if __name__ == "__main__":
    create_table()
    data = read_file_blob('image/python-logo.png')
    print(type(data))

    insert_query = "INSERT INTO images (name, pic) VALUES (%s, %s)"
    update_query = "UPDATE images SET name = %s, pic = %s WHERE no = %s"
    read_query = "SELECT pic FROM images WHERE no = %s"
    delete_qurey = "DELETE FROM images WHERE no = %s"
    selecct_query = "select no, name from images"

    insert_blob(insert_query, 'python-logo', 'image/python-logo.png')
    insert_blob(insert_query, 'google`-logo', 'image/google-logo.png')
    query_with_fetchall(selecct_query)
    print()

    read_blob(read_query, 1, "image/read-python.png")
    read_blob(read_query, 1, "image/read-google.png")

    update_blob(update_query, 'pycharm-logo', 'image/pycharm-logo.png', 1)
    query_with_fetchall(selecct_query)
    print()
    read_blob(read_query, 1, "image/read-pycharm.png")

    delete_blob(delete_qurey, 1)
    query_with_fetchall(selecct_query)