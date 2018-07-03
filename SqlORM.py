#coding:utf-8
'''
__title__: sql ORM,singleton
__author__:@lzy
__time__:2017.07.02
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

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBEngine():
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:Lieni!qwe521@192.168.0.149:3306/lieni?charset=utf8mb4',
                               pool_size =8)
        self.DBsession = sessionmaker(bind=self.engine)


DB_Singleton = DBEngine()









