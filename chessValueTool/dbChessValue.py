from sqlalchemy import (Text, Column, DateTime, ForeignKey, Index, Integer, String,
                        UniqueConstraint, create_engine, tuple_)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine(
    "mysql+pymysql://root:63632630@127.0.0.1:3306/chess?charset=utf8", max_overflow=50)
    # , encoding='utf-8')

Base = declarative_base()

class chessValue(Base):
    __tablename__ = 'chessValue'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fen = Column(String(128), nullable=False)
    value = Column(Integer, nullable=False)
    move = Column(String(1024), nullable=False)
    valueStr = Column((Text(256)), nullable=False)

# 日期：1993-04-30

if __name__ == "__main__":
    Base.metadata.drop_all(engine)   #删除表
    Base.metadata.create_all(engine)  #创建表