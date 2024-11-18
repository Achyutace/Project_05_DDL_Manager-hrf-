import os
import yaml

import mysql.connector
from mysql.connector import Error

from .query import query
from .add import add
from .adjust import adjust
from .delete import delete
from .show import process_command_show
from .utils import assert_command_format, print_help


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

