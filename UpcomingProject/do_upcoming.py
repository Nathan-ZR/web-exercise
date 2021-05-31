#!/usr/bin/env python
# -*- coding:utf-8 -*-
# file:do_upcoming.py
# author:张仁
# datetime:2021/5/25 14:40
# software: PyCharm
"""
    this is function description
"""
import json

from flask import Flask, render_template, request

from flask_bootstrap import Bootstrap
from UpcomingProject.Model.UpComingModel import Upcoming

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
        return json.dumps({})


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


@app.route('/allDataCount', methods=['GET'])
def allDataCount():
    try:
        results = Upcoming.selectAllRecord()
        total_count = len(results)
        Done_count = 0
        Undo_count = 0
        for record in results:
            if record.Undo:
                Undo_count += 1
            else:
                Done_count += 1
        count = {
            'total_count': total_count,
            'Done_count': Done_count,
            'Undo_count': Undo_count
        }
        return json.dumps({'count': count})
    except Exception as e:
        print(e)


@app.route('/insertData', methods=['POST'])
def insertData():
    try:
        Upcoming.insertRecord(request.args.get('condition'))
        records = json.loads(allData())
        count = json.loads(allDataCount())
        return json.dumps(dict(records, **count))

    except Exception as e:
        print(e)


@app.route('/removeData', methods=['POST'])
def removeData():
    try:
        Upcoming.deleteRecord(request.args.get('condition'))
        records = json.loads(allData())
        count = json.loads(allDataCount())
        return json.dumps(dict(records, **count))
    except Exception as e:
        print(e)


@app.route('/isFinish', methods=['POST'])
def isFinish():
    try:
        Upcoming.updateUndo(request.args.get('condition'), int(request.args.get('Undo')))
        records = json.loads(allData())
        count = json.loads(allDataCount())
        return json.dumps(dict(records, **count))
    except Exception as e:
        print(e)


@app.route('/editRecord', methods=['POST'])
def editRecord():
    try:
        Upcoming.updateTitle(request.args.get('condition'), request.args.get('newText'))
        records = json.loads(allData())
        count = json.loads(allDataCount())
        return json.dumps(dict(records, **count))
    except Exception as e:
        print(e)
