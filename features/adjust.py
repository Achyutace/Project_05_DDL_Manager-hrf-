from mysql.connector import Error
def adjust(conn):
    print("QUERY Ok, Now adjusting:[id] [new_deadline]")
    ans = input()
    id = ans.split()[0]
    nd = ans.split()[1]
    sql_com = "UPDATE ddl1 SET deadline = %s WHERE abs_id = %s"
    try:
        cursor = conn.cursor(buffered=True)
        cursor.execute(sql_com,(nd,id))
        conn.commit()
        print("ADJUST OK")
    except Error as e:
        print("Error101: Failed to Adjust ddl: ", e)
