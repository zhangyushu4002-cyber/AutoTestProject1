接口自动化测试框架

项目简介
本项目是基于 Python + pytest + requests 构建的接口自动化测试框架，实现了测试用例管理、数据驱动、日志记录和测试报告生成功能。框架采用分层设计，具有良好的可扩展性和可维护性。

技术栈
- Python 3.14
- pytest 7.4.0
- requests 2.31.0
- allure-pytest 2.13.2
- selenium 4.15.0
- PyYAML 6.0.1

项目结构
AutoTestProject1/
├── common/                    公共模块
│   ├── base_request.py        HTTP请求封装
│   ├── logger.py              日志系统
│   └── read_config.py         YAML配置读取
├── data/                      测试数据
│   ├── config.yaml            全局配置
│   └── api_case.yaml          接口测试数据
├── testcase/                  测试用例
│   ├── test_api.py            API接口测试
│   └── test_ui.py             UI自动化测试
├── page/                      Page Object模式
│   └── login_page.py          登录页面对象
├── log/                       日志文件
├── conftest.py                pytest配置
├── mock_server.py             Mock服务
├── requirements.txt           依赖包列表
├── run.py                     执行入口
└── README.md                  项目说明

快速开始

1. 安装依赖
   pip install -r requirements.txt

2. 启动Mock服务
   python mock_server.py

3. 执行测试
   python run.py

测试覆盖
- 登录接口：正常登录（正确账号密码）
- 登录接口：异常登录（错误密码）
- UI自动化：因无前端页面暂跳过

项目亮点
- 数据驱动：YAML管理测试数据，代码与数据分离
- 日志系统：控制台+文件双输出，按日期归档
- 框架分层：结构清晰，易于维护和扩展
- 请求封装：统一处理HTTP请求，接入成本低
- Mock服务：内置FastAPI Mock，独立运行

项目地址
https://github.com/zhangyushu4002-cyber/AutoTestProject1
