#!/usr/bin/env python
# -*- coding:utf-8 -*-
# file:__init__.py.py
# author:张仁
# datetime:2021/5/30 18:11
# software: PyCharm
"""
    this is function description
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from UpcomingProject.config import sqlConfig

__all__ = ['session']

# 创建引擎
engine = create_engine(
    sqlConfig.SQLALCHEMY_DATABASE_URI,
    pool_size=sqlConfig.POOL_SIZE,
    max_overflow=sqlConfig.MAX_OVERFLOW
)

# 创建会话对象
Session = sessionmaker(bind=engine)

# 创建会话实例
session = Session()
