#!/usr/bin/env python
# -*- coding:utf-8 -*-
# file:UpComingModel.py
# author:张仁
# datetime:2021/5/25 15:50
# software: PyCharm

from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base

from . import session

Base = declarative_base()
metadata = Base.metadata


class Upcoming(Base):
    __tablename__ = 'upcoming'

    autoID = Column(Integer, primary_key=True)
    Title = Column(String(255), nullable=False)
    Undo = Column(Integer, nullable=False, server_default=FetchedValue())

    @classmethod
    def selectRecord(cls, Title):
        """带条件查询"""
        try:
            results = []
            for record in session.query(cls).all():
                if Title in record.Title:
                    results.append(record)
            if len(results) > 0:
                return results
            else:
                session.rollback()
                raise Exception("The data is not found!")
        except Exception as e:
            print("Query Error:", e)

    @classmethod
    def selectAllRecord(cls):
        """不带条件的查询"""
        try:
            records = session.query(cls).all()
            if len(records) > 0:
                return records
            else:
                session.rollback()
                raise Exception("The data is not found!")
        except Exception as e:
            print("Query Error:", e)

    @classmethod
    def updateUndo(cls, Title, Undo):
        """更新数据Undo"""
        filter_list = []  # 条件判断
        try:
            if Title:
                assert isinstance(Title, str), "The type of Title should be str"
                filter_list.append(cls.Title == Title)
            if Undo:
                assert isinstance(Undo, int) and (Undo == 0 or Undo == 1), \
                    "The type of Undo should be int and the value must be 1 or 0 "
                filter_list.append(cls.Undo == Undo)
            # 更改为取反
            if Undo == 1:
                result = session.query(cls).filter(*filter_list).update({'Undo': 0})
            else:
                result = session.query(cls).filter(*filter_list).update({'Undo': 1})
            if result > 0:
                session.commit()
            else:
                session.rollback()
                raise Exception("The data is not found!")
        except Exception as e:
            print("Update Error:", e)

    @classmethod
    def updateTitle(cls, oldTitle, newTitle):
        """更新数据Title"""
        try:
            if oldTitle:
                assert isinstance(oldTitle, str), "The type of Title should be str"
            result = session.query(cls).filter(cls.Title == oldTitle).update({'Title': newTitle})
            if result > 0:
                session.commit()
            else:
                session.rollback()
                raise Exception("The data is not found!")
        except Exception as e:
            print("Update Error:", e)

    @classmethod
    def deleteRecord(cls, Title):
        """删除数据记录"""
        try:
            if Title:
                assert isinstance(Title, str), "The type of Title should be str"
            session.delete(session.query(cls).filter(cls.Title == Title).first())
            session.commit()
        except Exception as e:
            print("Delete Error:", e)

    @classmethod
    def insertRecord(cls, Title):
        """插入数据"""
        try:
            if not Title:
                raise Exception("Title must be filled")
            record = Upcoming(Title=Title)
            session.add(record)
            session.commit()
        except Exception as e:
            print("Insert Error:", e)
