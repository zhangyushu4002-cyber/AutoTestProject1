import yaml
import os

def read_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# 项目根目录绝对路径（彻底修复换环境报错）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(BASE_DIR, "data", "config.yaml")
CASE_PATH = os.path.join(BASE_DIR, "data", "api_case.yaml")

config = read_yaml(CONFIG_PATH)