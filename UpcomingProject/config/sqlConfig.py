#!/usr/bin/env python
# -*- coding:utf-8 -*-
# file:sqlConfig.py
# author:张仁
# datetime:2021/5/25 14:40
# software: PyCharm
"""
    数据库的配置文件
"""
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'zr192837'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'python_homework'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 数据库连接池初始化的容量
POOL_SIZE = 5

# 连接池最大溢出容量，该容量+初始容量=最大容量。超出会堵塞等待，等待时间为timeout参数值默认30
MAX_OVERFLOW = 10
