#coding:utf-8
'''
__title__: sql cv class
__author__:@lzy
__time__:2018.07.03
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

from database.SqlIHandler import ISql
from util import ConfigReader

class CVSqlAdd(ISql):
    def __init__(self):
        ISql.__init__(self)

    def get_sql(self):
        pass



class CVSqlTotal(ISql):
    def __init__(self):
        ISql.__init__(self)
        self.process_size = int(ConfigReader.getConfigParser('queue', 'cv_process_num'))