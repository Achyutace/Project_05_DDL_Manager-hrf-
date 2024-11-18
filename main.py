import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

from features import *
"""
config = {
    host: localhost
    user: root
    password: your password
    database: try "ddl_manager"
}
"""

def run():
    command = input()
    kw = command.split()

    if kw[0] == "HELP":
        print_help()
    
    # check whether args is valid
    try:
        assert_command_format(kw)
    except AssertionError as e:
        print(e)

    if len(kw) == 2:
        fw,sw = kw

        if fw == "ADJUST":
            adjust(conn)

        if fw == "ADD" :
            add(conn,fw,sw)

        if fw == "QUERY":
            query(conn,fw,sw)

        if fw == "DELETE":
            if sw == "YIELD" or sw == "YIELDS":
                print("DELETE REQUEST Ok, input name")
                para = input()
                sql_com = "DELETE FROM YIELDS1 WHERE name = %s"
                try:
                    cursor = conn.cursor(buffered=True)
                    cursor.execute(sql_com, (para,))
                    conn.commit()
                    print("deleted successfully")
                except Error as e:
                    print("Error 202: Failed to delete: ", e)
            if sw == "DDL" or sw == "DDLS":
                print("DELETE REQUEST Ok, input name")
                para = input()
                sql_com = "DELETE FROM ddl1 WHERE name = %s"
                try:
                    cursor = conn.cursor(buffered=True)
                    cursor.execute(sql_com, (para,))
                    conn.commit()
                    print("deleted successfully")
                except Error as e:
                    print("Error 202: Failed to delete: ", e)

    if len(kw) == 3:
        process_command_show(conn, kw)

def main():
    while True:
        run()

if __name__ == "__main__":
    main()

# 确保在程序退出时关闭数据库连接
if conn:
    conn.close()