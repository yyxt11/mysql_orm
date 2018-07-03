
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,INT,VARCHAR,BIGINT,TEXT
# 创建对象的基类:
Base = declarative_base()

class cvResumeInfo(Base):
    __tablename__ = 'T_CV_RESUME_INFO'
    ID = Column(VARCHAR(15), primary_key=True,autoincrement=True)
    Degree = Column(INT(2),nullable=False,default=0)
    WorkCity = Column(BIGINT(20),nullable=False,default=0)
    Gender = Column(INT(2),nullable=False,default=-1)
    Marital = Column(INT(2),nullable=False,default=-0)
    BirthYear = Column(INT(4))
    WorkState = Column(INT(2),nullable=False,default=-0)
    CureentSalary = Column(INT(11))

class cvEducationExp(Base):
    __tablename__ = 'T_CV_EDUCATION_EXPERIENCE'
    ID = Column(INT(11), primary_key=True, autoincrement=True)
    ResumeID = Column(VARCHAR(15))
    School = Column(VARCHAR(400))
    EndYear = Column(INT(4))
    EndMonth = Column(INT(2))

class cvWorkExp(Base):
    __tablename__ = 'T_CV_WORK_EXPERIENCE'
    ID = Column(INT(11), primary_key=True, autoincrement=True)
    ResumeID = Column(VARCHAR(15))
    Company = Column(VARCHAR(250))
    DutyPerformance = Column(TEXT())
    CompanyIndustry = Column(VARCHAR(50))
    CompanyIntrdouce = Column(VARCHAR(2000))
    JobName =  Column(VARCHAR(100))
    StartYear = Column(INT(4))
    StartMonth = Column(INT(2))
    EndYear = Column(INT(4))
    EndMonth = Column(INT(2))

class Job(Base):
    __tablename__ = 'T_JOB'
    ID = Column(BIGINT(20),primary_key=True,autoincrement=True)
    Title = Column(VARCHAR(50),nullable=False)
    Description = Column(VARCHAR(2000),nullable=False)
    Requirement = Column(VARCHAR(2000),nullable=False)