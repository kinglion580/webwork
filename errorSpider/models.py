from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

engine = create_engine('mysql+mysqldb://root@localhost:3306/course?charset=utf8')
Base = declarative_base()

class CourseError(Base):
    __tablename__ = 'question'
    
    id = Column(Integer,primary_key=True)
    userHref = Column(String(64))
    title = Column(String(1024))
    userId = Column(String(64))
    username = Column(String(64)) 
    level = Column(Integer) 
    date = Column(String(64))
    courseHref = Column(String(64))
    coursename = Column(String(64))
    answered = Column(Integer)
    viewed = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)

