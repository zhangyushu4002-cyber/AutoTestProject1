import logging
import os
from datetime import datetime

# 自动获取项目根目录（终极适配，换环境不报错）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(BASE_DIR, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

LOG_FILE = os.path.join(LOG_PATH, f"{datetime.now().strftime('%Y%m%d')}.log")

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.logger = logging.getLogger("AutoTest")
            cls.logger.setLevel(logging.INFO)
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
            file_handler.setFormatter(formatter)
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            cls.logger.addHandler(file_handler)
            cls.logger.addHandler(stream_handler)
        return cls._instance

log = Logger().logger