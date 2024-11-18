def print_help():
    print("Available commands:")
    print("  ADD YIELD/DDL")
    print("  ADJUST DDL")
    print("  QUERY YIELD/DDLS/ALL")
    print("  DELETE YIELD/DDL")
    print("  SHOW DEADLINE ASC/DESC")
    print("  SHOW IMPORTANCE ASC/DESC")
    print("  SHOW DIFFICULTY ASC/DESC")
    print("  SHOW TIME ASC/DESC")
    print("  SHOW GROUP ASC/DESC")

def assert_command_format(*args):
    valid_commands = {
        "HELP": [],
        "ADD": ["YIELD", "DDL", "DDLS"],
        "ADJUST": ["DDL", "DDLS"],
        "QUERY": ["YIELD", "DDL", "DDLS", "ALL"],
        "DELETE": ["YIELD", "DDL", "DDLS"],
        "SHOW": {
            "DEADLINE": ["ASC", "DESC"],
            "IMPORTANCE": ["ASC", "DESC"],
            "DIFFICULTY": ["ASC", "DESC"],
            "TIME": ["ASC", "DESC"],
            "GROUP": ["ASC", "DESC"]
        }
    }
    
    if args[0] in {"HELP"}:
        assert len(args)==1, "Invalid command."
    # 至少需要两个参数（命令和子命令）
    assert len(args) >= 2, "Not enough arguments provided."
    
    fw, sw = args[0], args[1]

    # 检查第一个单词是否为有效命令
    assert fw in valid_commands, f"Invalid command: {fw}"

    # 检查第二个单词是否为有效子命令
    if fw in ["ADD", "ADJUST", "QUERY", "DELETE"]:
        assert sw in valid_commands[fw], f"Invalid sub-command: {sw}"
    elif fw == "SHOW":
        assert sw in valid_commands[fw], f"Invalid sub-command for 'SHOW': {sw}"
        lw = args[2] if len(args) > 2 else None
        assert lw in valid_commands[fw][sw], f"Invalid order for 'SHOW {sw}': {lw}"

# 示例使用断言式
try:
    assert_command_format("SHOW", "DEADLINE", "ASC")
    print("Command format is correct.")
except AssertionError as e:
    print(e)
