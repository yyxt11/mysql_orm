#coding:utf-8
'''
__title__: sql cv class
__author__:@lzy
__time__:2010.07.03
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

from database.SqlIHandler import ISql,Job,cvEducationExp,cvResumeInfo,cvWorkExp,cvResumeInfo
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import Insert
import logging
import pandas as pd
logger = logging.getLogger('__main__')


@compiles(Insert)
def append_string(insert, compiler, **kw):
    s = compiler.visit_insert(insert, **kw)
    if 'append_string' in insert.kwargs:
        return s + " " + insert.kwargs['append_string']
    return s

#JOB全量更新实体类
class JOBSqlTotal(ISql):
    def __init__(self):
        ISql.__init__(self)

    def select_db(self,*args):

        try:
            query = self.session.query(Job).statement
            result = pd.read_sql(query,self.session.bind)
            return result
        except Exception as err:
            logger.error('job全量更新读取数据库失败,原因：{0},query:{1}'.format(err,query))


    def update_db(self, data):

        param = data.values.tolist()
        try:
            self.cur.executemany(sql, param)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            logger.exception(
                'insert fail,id from {0} to {1},num {2},cause {3}'.format(param[0], param[-1], len(param), e))
        else:
            logger.info('sql:{0},data{1}'.format(sql, data.loc[0]))
        return



#JOB增量更新实体类
class JOBSqlAdd(ISql):
    def __init__(self):
        ISql.__init__(self)

    def select_db(self,*args):
        for id in args:
            try:
                query = self.session.query(Job).filter(Job.ID == id).statement
                result = pd.read_sql(query, self.session.bind)
                return result
            except Exception as err:
                logger.error('job增量更新读取数据库失败,id:{0}原因：{1},query:{2}'.format(id,err, query))



    def update_db(self,*args):
        return