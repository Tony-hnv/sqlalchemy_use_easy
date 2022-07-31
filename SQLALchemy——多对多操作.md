# SQLALchemy——多对多操作

### 1. 创建表及关系

```python
# create_m2m.py

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

class Hotel(Base):
 __tablename__="hotel"
 id=Column(Integer,primary_key=True)
 girl_id = Column(Integer,ForeignKey("girl.id"))
 boy_id = Column(Integer,ForeignKey("boy.id"))

class Girl(Base):
 __tablename__="girl"
 id=Column(Integer,primary_key=True)
 name = Column(String(32),index=True)

 #创建关系
 boys = relationship("Boy",secondary="hotel",backref="girl2boy")


class Boy(Base):
 __tablename__="boy"
 id=Column(Integer,primary_key=True)
 name = Column(String(32),index=True)


from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:DragonFire@127.0.0.1:3306/dragon?charset=utf8")

Base.metadata.create_all(engine)

```



### 2. 基于relationship增加数据

```python
# crud_insert_m2m.py

from my_M2M import Girl,Boy,Hotel,engine
 
# 创建连接
from sqlalchemy.orm import sessionmaker
# 创建数据表操作对象 sessionmaker
DB_session = sessionmaker(engine)
db_session = DB_session()

# 1.通过Boy添加Girl和Hotel数据
boy = Boy(name="DragonFire")
boy.girl2boy = [Girl(name="赵丽颖"),Girl(name="Angelababy")]
db_session.add(boy)
db_session.commit()

# 2.通过Girl添加Boy和Hotel数据
girl = Girl(name="珊珊")
girl.boys = [Boy(name="Dragon")]
db_session.add(girl)
db_session.commit()

```



### 3. 基于relationship查询数据

```python
# ocrud_select_m2m.py

from my_M2M import Girl,Boy,Hotel,engine

# 创建连接
from sqlalchemy.orm import sessionmaker
# 创建数据表操作对象 sessionmaker
DB_session = sessionmaker(engine)
db_session = DB_session()
 
# 1.通过Boy查询约会过的所有Girl
hotel = db_session.query(Boy).all()
for row in hotel:
  for row2 in row.girl2boy:
    print(row.name,row2.name)

# 2.通过Girl查询约会过的所有Boy
hotel = db_session.query(Girl).all()
for row in hotel:
 for row2 in row.boys:
  print(row.name,row2.name)

```

