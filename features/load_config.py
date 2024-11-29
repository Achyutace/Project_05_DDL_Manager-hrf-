import os
import yaml

config_path = f"{os.path.dirname(os.path.dirname(__file__))}/config/application.yaml"


# os.chdir(os.path.dirname(os.getcwd()))
# print(os.getcwd())
def load_config(filename=config_path):
    with open(filename, 'r') as file:
        return yaml.safe_load(file)

config = load_config()
mysql_config = config.get('mysql')
llm_config = config.get('LLM')

