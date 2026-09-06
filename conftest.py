import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from common.base_request import req
from common.read_config import read_yaml, BASE_DIR
from common.logger import log

# 绝对路径读取用python mock_server.py例，彻底杜绝找不到文件
case_data = read_yaml(os.path.join(BASE_DIR, "data", "api_case.yaml"))

@pytest.fixture(scope="function")
def api_fixture():
    log.info("===== 开始执行接口用例 =====")
    yield req
    log.info("===== 接口用例执行结束 =====")

@pytest.fixture(scope="function")
def driver():
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    # 无界面后台运行，不需要弹出浏览器窗口，不会崩溃
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
