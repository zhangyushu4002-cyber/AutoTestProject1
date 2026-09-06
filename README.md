# 接口自动化测试框架

## 项目简介
本项目是基于 Python + pytest + requests 构建的接口自动化测试框架，实现了测试用例管理、数据驱动、日志记录和测试报告生成功能。

## 技术栈
- Python 3.14
- pytest 7.4.0
- requests 2.31.0
- allure-pytest 2.13.2
- selenium 4.15.0
- PyYAML 6.0.1

## 项目结构
```
AutoTestProject1/
├── common/
│   ├── base_request.py
│   ├── logger.py
│   └── read_config.py
├── data/
│   ├── config.yaml
│   └── api_case.yaml
├── testcase/
│   ├── test_api.py
│   └── test_ui.py
├── page/
│   └── login_page.py
├── log/
├── conftest.py
├── mock_server.py
├── requirements.txt
├── run.py
└── README.md
```

## 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 启动Mock服务
```bash
python mock_server.py
```

### 执行测试
```bash
python run.py
```

## 测试覆盖
- 登录接口：正常登录
- 登录接口：异常登录
- UI自动化：暂跳过

## 项目亮点
- 数据驱动
- 日志系统
- 框架分层
- Mock服务

## 项目地址
https://github.com/zhangyushu4002-cyber/AutoTestProject1
