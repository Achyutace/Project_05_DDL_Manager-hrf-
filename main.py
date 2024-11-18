import yaml
import os
import mysql.connector
from mysql.connector import Error
from tabulate import tabulate
from features.utils import *
from features.show import process_command_show
from features.adjust import adjust
from features.add import add
"""
config = {
    host: localhost
    user: root
    password: your password
    database: try "ddl_manager"
}
"""
config_path = "config/application.yaml"

# os.chdir(os.path.dirname(os.getcwd()))
print(os.getcwd())
def load_config(filename=config_path):
    with open(filename, 'r') as file:
        return yaml.safe_load(file)

config = load_config()
mysql_config = config.get('mysql')
# 全局变量来存储数据库连接和游标
conn = None
cursor = None


def create_database(db_config, database_name):
    try:
        conn = mysql.connector.connect(**db_config)
        print("Connected to MySQL server")
        cursor = conn.cursor()

        cursor.execute("SHOW DATABASES")
        db_exists = database_name in [db[0] for db in cursor.fetchall()]

        if not db_exists:
            cursor.execute(f"CREATE DATABASE {database_name}")
            print(f"Database '{database_name}' created")
        else:
            print(f"Database '{database_name}' already exists")

        cursor.close()
        conn.close()

    except Error as e:
        print("Error while connecting to MySQL server", e)
    finally:
        if conn:
            conn.close()


# 创建数据库
create_database({
    'host': mysql_config['host'],
    'user': mysql_config['user'],
    'password': mysql_config['password']
}, mysql_config['database'])

# 连接到 MySQL 数据库

try:
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()
    print(f"Successfully connected to database : {mysql_config['database']}")
except Error as e:
    print("Error000: Error while connecting to MySQL", e)
    conn = None

# 创建DDL表
ddl_table_query = """
CREATE TABLE IF NOT EXISTS ddl1 (
    abs_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    yields VARCHAR(255) NOT NULL,
    deadline DATE NOT NULL,
    importance INT NOT NULL,
    difficulty INT NOT NULL,
    estimate INT NOT NULL
);
"""

yields_table_query = """
CREATE TABLE IF NOT EXISTS YIELDS1 (
    abs_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
"""

if conn:
    try:
        cursor.execute(ddl_table_query)
        cursor.execute(yields_table_query)
        print("DDL and YIELDS tables exist or have been created successfully.")
    except Error as e:
        print("Error007: Failed to create table", e)




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
            if fw == "QUERY" and (sw == "YIELD" or sw == "YIELDS"):
                sql_com = "SELECT * FROM YIELDS1"
            if fw == "QUERY" and (sw == "DDL" or sw == "DDLS"):
                sql_com = "SELECT * FROM ddl1"
            if fw == "QUERY" and sw == "ALL":
                sql_com = "SELECT * FROM ddl1 LEFT JOIN YIELDS1 ON ddl1.yields = YIELDS1.name"
            try:
                cursor = conn.cursor(buffered=True)
                cursor.execute(sql_com)
                rows = cursor.fetchall()
                # 获取列名
                column_names = [i[0] for i in cursor.description]
                # 使用tabulate来格式化输出
                print(tabulate(rows, headers=column_names, tablefmt="grid"))
            except Error as e:
                print("Error201 : Failed to query DDL: ", e)
            finally:
                if cursor:
                    cursor.close()

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