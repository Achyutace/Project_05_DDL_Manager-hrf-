import yaml

# 配置信息
config = {
    "LLM":{
        "api_base":"https://api.deepseek.com",
        "api_key":"sk-c853f9a55e014ad8ba2f6df21817ac13",
        "name":"ddl_manager",
        "moudle":"deepseek-chat"
    },
    "mysql":{
        'host': 'localhost',
        'user': 'root',
        'password': 'AcCe_142857_', #填密码
        'database': 'ddl_manager',
    }
    
    
}

# 将配置信息写入 YAML 文件
def write_config_to_yaml(config, filepath="config/application.yaml"):
    with open(filepath, 'w') as file:
        yaml.dump(config, file, default_flow_style=False)

# 调用函数
write_config_to_yaml(config)