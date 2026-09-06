接口自动化测试框架

项目简介
本项目是基于 Python + pytest + requests 构建的接口自动化测试框架，实现了测试用例管理、数据驱动、日志记录和测试报告生成功能。框架采用分层设计，具有良好的可扩展性和可维护性。

技术栈
Python 3.14
pytest 7.4.0
requests 2.31.0
allure-pytest 2.13.2
selenium 4.15.0
PyYAML 6.0.1

项目结构
AutoTestProject1/
├── common/                   公共模块
│   ├── base_request.py       HTTP请求封装（GET/POST/PUT/DELETE）
│   ├── logger.py             日志系统（控制台+文件双输出）
│   └── read_config.py        YAML配置文件读取
├── data/                     测试数据目录
│   ├── config.yaml           全局配置（环境地址、用户信息）
│   └── api_case.yaml         接口测试用例数据
├── testcase/                 测试用例目录
│   ├── test_api.py           API接口自动化测试
│   └── test_ui.py            UI自动化测试（预留）
├── page/                     Page Object模式
│   └── login_page.py         登录页面对象封装
├── log/                      日志文件存储目录
├── .idea/                    PyCharm项目配置
├── conftest.py               pytest fixture配置
├── mock_server.py            Mock服务（模拟后端接口）
├── requirements.txt          项目依赖包列表
├── run.py                    测试执行入口
└── README.md                 项目说明文档

快速开始

1. 安装依赖包
pip install -r requirements.txt

2. 启动Mock服务（模拟后端接口）
python mock_server.py

3. 执行所有测试用例
python run.py

或者使用pytest命令：
pytest -v -s

4. 生成Allure测试报告
pytest --alluredir=./allure-results
allure serve ./allure-results

测试覆盖

登录接口测试
- 正常登录：正确账号密码，预期返回200和登录成功
- 异常登录：错误密码，预期返回500和密码错误

UI自动化测试
- 登录页面测试：当前因无前端页面而跳过

项目亮点

1. 数据驱动：使用YAML文件管理测试数据，新增用例无需修改代码

2. 日志系统：采用单例模式实现日志记录，支持控制台和文件双通道输出，按日期自动归档

3. 框架分层：分为base层（请求封装）、common层（公共工具）、data层（测试数据）、testcase层（测试用例），代码结构清晰，易于维护

4. 请求封装：统一封装HTTP请求方法，集成超时控制、异常捕获和日志记录，新接口接入成本低

5. Mock服务：内置FastAPI Mock服务器，不依赖真实后端即可独立运行测试

6. 扩展性强：目前支持API接口测试，同时预留了Selenium UI自动化测试能力

待优化项

- 增加更多业务模块的接口测试用例
- 集成Jenkins实现持续集成
- 添加接口依赖链测试（如登录后获取用户信息）
- 增加邮件通知功能

联系方式

GitHub: https://github.com/zhangyushu4002-cyber
项目地址: https://github.com/zhangyushu4002-cyber/AutoTestProject1
