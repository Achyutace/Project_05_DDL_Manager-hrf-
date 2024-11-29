from features import *
def run():
    command = input()
    kw = list(map(lambda w:w.upper(), command.split()))
    if kw[0] == "HELP":
        print_help()

    # check whether args is valid
    try:
        assert_command_format(kw)
    except AssertionError as e:
        print(e)
    switch_dict = {
    2: {
        "ADJUST": lambda: adjust(conn),
        "ADD": lambda: add(conn, fw, sw),
        "QUERY": lambda: query(conn, fw, sw),
        "DELETE": lambda: delete(conn, fw, sw)
    },
    3: lambda: process_command_show(conn, kw)
}
    length = len(kw)
    if length == 2:
        fw, sw = kw
        action = switch_dict[2].get(fw)
        if action:
            action()
    elif length == 3:
        switch_dict[3]()

def main():
    while True:
        run()

if __name__ == "__main__":
    print(mysql_config)
    main()

# 确保在程序退出时关闭数据库连接
if conn:
    conn.close()