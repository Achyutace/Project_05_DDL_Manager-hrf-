from mysql.connector import Error

def add(conn, fw, sw):
    # 添加YIELD记录

    if fw == "ADD" and (sw == "YIELD" or sw == "YIELDS"):
        print("QUERY Ok, Now adding:[name]")
        name = input()
        sql_com = "INSERT INTO YIELDS1(name) VALUES(%s)"
        try:
            cursor = conn.cursor(buffered=True)
            cursor.execute(sql_com, (name,))
            conn.commit()
            print("YIELD added successfully")
        except Error as e:
            print("Error101: Failed to insert YIELD: ", e)

    # 添加DDL记录
    if fw == "ADD" and (sw == "DDL" or sw == "DDLS"):
        print("QUERY Ok, Now adding:[name] [yields] [deadline] [importance] [difficulty] [estimate]")
        data = input().split()
        name, yields, deadline, importance, difficulty, estimate = data
        sql_com = """
        INSERT INTO ddl1(name, yields, deadline, importance, difficulty, estimate)
        VALUES(%s, %s, %s, %s, %s, %s)
        """
        try:
            cursor = conn.cursor(buffered=True)
            cursor.execute(sql_com, (name, yields, deadline, importance, difficulty, estimate))
            conn.commit()
            print("DDL added successfully")
        except Error as e:
            print("Error102: Failed to insert DDL: ", e)
