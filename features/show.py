import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

def execute_query(conn, sql_com):
    try:
        cursor = conn.cursor(buffered=True)
        cursor.execute(sql_com)
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        print(tabulate(rows, headers=column_names, tablefmt="grid"))
    except Error as e:
        print("Error301 : Failed to query DDL: ", e)
    finally:
        if cursor:
            cursor.close()

def generate_sql_command(mw, lw):
    sql_commands = {
        ("DEADLINE", "ASC"): "SELECT * FROM ddl1 ORDER BY deadline ASC",
        ("DEADLINE", "DESC"): "SELECT * FROM ddl1 ORDER BY deadline DESC",
        ("IMPORTANCE", "ASC"): "SELECT * FROM ddl1 ORDER BY importance ASC",
        ("IMPORTANCE", "DESC"): "SELECT * FROM ddl1 ORDER BY importance DESC",
        ("DIFFICULTY", "ASC"): "SELECT * FROM ddl1 ORDER BY difficulty ASC",
        ("DIFFICULTY", "DESC"): "SELECT * FROM ddl1 ORDER BY difficulty DESC",
        ("TIME", "ASC"): "SELECT * FROM ddl1 ORDER BY estimate ASC",
        ("TIME", "DESC"): "SELECT * FROM ddl1 ORDER BY estimate DESC",
        ("GROUP", "ASC"): "SELECT yields AS yield, SUM(estimate) AS total_time FROM ddl1 GROUP BY yield ORDER BY total_time ASC",
        ("GROUP", "DESC"): "SELECT yields AS yield, SUM(estimate) AS total_time FROM ddl1 GROUP BY yield ORDER BY total_time DESC"
    }
    return sql_commands.get((mw, lw))

def process_command_show(conn, kw):

    fw, mw, lw = kw
    sql_com = generate_sql_command(mw, lw)
    if sql_com:
        execute_query(conn, sql_com)
    else:
        print(f"Error003: Invalid command: {mw} {lw}. Use 'HELP' for assistance.")

# Example usage
if __name__ == "__main__":
    conn = mysql.connector.connect(host='localhost', database='your_database', user='your_username', password='your_password')
    if conn.is_connected():
        process_command_show(conn, ["SHOW", "DEADLINE", "ASC"])
        conn.close()