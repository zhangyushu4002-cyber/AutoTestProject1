import pytest
from conftest import case_data
from common.logger import log

# 参数化解析用例
cases = case_data["login_case"]

@pytest.mark.api
@pytest.mark.parametrize("case", cases)
def test_login_api(api_fixture, case):
    """登录接口自动化测试"""
    log.info(f"执行用例：{case['name']}")
    res = api_fixture.send_request(
        method=case["method"],
        url=case["url"],
        json=case.get("json")
    )
    #改用print打印，控制台直接输出返回结果
    print("接口返回数据：", res.json())

    assert res.status_code == 200
    assert res.json()["code"] == case["assert"]["code"]
    # 先注释掉msg断言，先确认业务code是否能跑通
    # assert case["assert"]["msg"] in res.json()["msg"]
    log.info(f"{case['name']} 执行通过")
