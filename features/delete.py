from mysql.connector import Error

def delete_record(conn, table_name, column_name):
    print(f"DELETE REQUEST Ok, input {column_name}")
    para = input()
    sql_com = f"DELETE FROM {table_name} WHERE {column_name} = %s"
    try:
        with conn.cursor(buffered=True) as cursor:
            cursor.execute(sql_com, (para,))
            conn.commit()
            print("deleted successfully")
    except Error as e:
        print(f"Error 202: Failed to delete from {table_name}: {e}")
def delete(conn, fw, sw):
    if sw == "YIELD" or sw == "YIELDS":
        delete_record(conn, "YIELDS1", "name")

    if sw == "DDL" or sw == "DDLS":
        delete_record(conn, "ddl1", "name")