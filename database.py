from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INT, VARCHAR, DECIMAL
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
  __tablename__ = 'user'
  uid = Column(INT, primary_key=True)
  name = Column(VARCHAR(32), index=True)
  department = Column(VARCHAR(20))


class Item(Base):
  __tablename__ = 'item'
  iid = Column(INT, primary_key=True)
  name = Column(VARCHAR(32), index=True)
  location = Column(VARCHAR(20), index=True)
  prince = Column(DECIMAL(10,2))

engine = create_engine('mysql+pymysql://root:root@localhost:3306/fast_demo?charset=utf8')
Base.metadata.create_all(engine)
