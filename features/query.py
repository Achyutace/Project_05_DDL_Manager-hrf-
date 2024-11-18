from mysql.connector import Error
from tabulate import tabulate

def query(conn, fw, sw):
    sql_com = ""
    
    if fw == "QUERY":
        if sw in ["YIELD", "YIELDS"]:
            sql_com = "SELECT * FROM YIELDS1"
        elif sw in ["DDL", "DDLS"]:
            sql_com = "SELECT * FROM ddl1"
        elif sw == "ALL":
            sql_com = "SELECT * FROM ddl1 LEFT JOIN YIELDS1 ON ddl1.yields = YIELDS1.name"
    
    if not sql_com:
        print("Error202: Invalid query parameters")
        return
    
    try:
        with conn.cursor(buffered=True) as cursor:
            cursor.execute(sql_com)
            rows = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            print(tabulate(rows, headers=column_names, tablefmt="grid"))
    except Error as e:
        print(f"Error201: Failed to query DDL: {e}")

# 示例调用
# execute_query(conn, "QUERY", "YIELD")