import requests
from common.logger import log
from common.read_config import config

class BaseRequest:
    def __init__(self):
        self.host = config["host"]
        self.headers = {"Content-Type": "application/json"}
        self.token = ""

    def set_token(self, token):
        """全局设置token"""
        self.token = token
        self.headers["Authorization"] = f"Bearer {self.token}"

    def send_request(self, method, url, json=None, params=None):
        """统一请求封装，处理异常、日志、响应"""
        url = self.host + url
        try:
            if method.upper() == "GET":
                res = requests.get(url, headers=self.headers, params=params, timeout=10)
            elif method.upper() == "POST":
                res = requests.post(url, headers=self.headers, json=json, timeout=10)
            elif method.upper() == "PUT":
                res = requests.put(url, headers=self.headers, json=json, timeout=10)
            elif method.upper() == "DELETE":
                res = requests.delete(url, headers=self.headers, json=json, timeout=10)
            else:
                log.error("不支持的请求方式")
                return None
            log.info(f"请求地址:{url}, 请求方式:{method}, 响应码:{res.status_code}")
            return res
        except Exception as e:
            log.error(f"请求异常：{str(e)}")
            return None

# 全局请求实例
req = BaseRequest()