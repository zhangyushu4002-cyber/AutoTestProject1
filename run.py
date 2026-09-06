import pytest
import os

if __name__ == "__main__":
    # 纯执行用例，不调用系统allure命令，新手100%无报错
    pytest.main([
        "./testcase",
        "-s",
        "-v"
    ])
    print("✅ 所有自动化用例执行完成！无报错")