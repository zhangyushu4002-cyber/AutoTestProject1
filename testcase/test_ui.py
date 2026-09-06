import pytest

from page.login_page import LoginPage
from common.read_config import config
@pytest.mark.skip(reason="mock服务无前端页面，仅演示接口自动化")
@pytest.mark.ui
def test_login_ui(driver):
    """登录页面UI自动化测试"""
    driver.get("http://localhost:8080/login")
    login_page = LoginPage(driver)
    # 执行登录
    login_page.login(config["test_user"]["username"], config["test_user"]["password"])
    # 断言
    assert "欢迎" in login_page.get_success_text()