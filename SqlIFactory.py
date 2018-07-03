#coding:utf-8
'''
__title__: sql factory
__author__:@lzy
__time__:2018.07.02
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
'''
from database.SqlCVHandler import CVSqlAdd,CVSqlTotal
from database.SqlJOBHandler import JOBSqlAdd,JOBSqlTotal


class IFactory():
    def __init__(self):
        self.sqlclass = None

    def from_db(self):
        raise NotImplementedError

    def to_db(self):
        raise NotImplementedError

    def from_db(self):
        self.sqlclass.select_db()

    def to_db(self):
        self.sqlclass.update_db()

class CVFactoryTotal(IFactory):
    def __init__(self):
        self.sqlclass = CVSqlTotal

class CVFactoryAdd(IFactory):
    def __init__(self):
        self.sqlclass = CVSqlAdd

class JOBFactoryTotal(IFactory):
    def __init__(self):
        self.sqlclass = JOBSqlTotal


class JOBFactoryAdd(IFactory):
    def __init__(self):
        self.sqlclass = JOBSqlAdd

