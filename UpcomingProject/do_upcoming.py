#!/usr/bin/env python
# -*- coding:utf-8 -*-
# file:do_upcoming.py
# author:张仁
# datetime:2021/5/25 14:40
# software: PyCharm
"""
    利用Python+flask框架，实现一个代办事情（需要有：编号，代办事情标题，时间 ，状态等字段）列表web应用；
    技术要点：
    1 界面可以选用前端UI框架；可以采用前后端分离的方式实现，也可以混编方式实现；
    2 数据库采用MySQL;采用SQLAchemy框架；
"""
import json

from flask import Flask, render_template, request

from flask_bootstrap import Bootstrap
from .Model.UpComingModel import Upcoming


# 创建flask应用对象
app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/data', methods=['GET', 'POST'])
def data():
    try:
        results = Upcoming.selectRecord(request.args.get('condition'))
        records = []
        for record in results:
            info = {
                'autoID': record.autoID,
                'Title': record.Title,
                'Undo': record.Undo
            }
            records.append(info)
        return json.dumps({'records': records})
    except Exception as e:
        return json.dumps({'records': []})


@app.route('/allData', methods=['GET'])
def allData():
    try:
        results = Upcoming.selectAllRecord()
        records = []
        for record in results:
            info = {
                'autoID': record.autoID,
                'Title': record.Title,
                'Undo': record.Undo
            }
            records.append(info)
        return json.dumps({'records': records})
    except Exception as e:
        print(e)


@app.route('/insertData', methods=['POST'])
def insertData():
    try:
        Upcoming.insertRecord(request.args.get('condition'))
        return allData()
    except Exception as e:
        print(e)


@app.route('/removeData', methods=['POST'])
def removeData():
    try:
        Upcoming.deleteRecord(request.args.get('condition'))
        return allData()
    except Exception as e:
        print(e)


@app.route('/isFinish', methods=['POST'])
def isFinish():
    try:
        Upcoming.updateUndo(request.args.get('condition'),
                            int(request.args.get('Undo')))
        return allData()
    except Exception as e:
        print(e)


@app.route('/editRecord', methods=['POST'])
def editRecord():
    try:
        Upcoming.updateTitle(request.args.get('condition'),
                             request.args.get('newText'))
        return allData()
    except Exception as e:
        print(e)
