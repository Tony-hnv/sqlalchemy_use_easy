# SQLAlchemy多表操作

### 1. 创建多表

```python
# create_table_ForeginKey.py

from sqlalchemy.ext.declarative import declarative_base
from salalchemy import Column, INT, VARCHAR, ForeignKey
from sqlalchemy import create_engine

Base = declarative_base()

class Student(Base):
  __tablename__ = 'student'
  id = Column(INT, primary_key=True)
  name = Column(VARCHAR(32))
  school_id = Column(INT, ForeignKey('school.id'))
  
class School(Base):
  __tablename__ = 'school'
  id = Column(INT, primary_key=True)
  name = Column(VARCHAR(32))
  
  
engine = create_engine('mysql+pymysql://root:root@localhost:3306/fast_demo?charset=utf8')
Base.metadata.create_all(engine)
```

### 2. 多表insert

#### 1.原始增加数据 （笨）

```python
# crud_insert_ForeignKey.py

from sqlalchemy.orm import sessionmaker
from create_table_ForeignKey import engine

Session = sessionmaker(engine)
db_session = Session()

sch_obj = School(name='pekingUniversity')
db_session.add(sch_obj)
db_session.commit()
db_session.close()

sch_obj = db_session.query(School).filter(School.name == 'pekingUniversity').first()
stu_obj = Student(name='zs', school_id=sch_obj.id)

db_session.add(stu_obj)
db_session.commit()
db_session.close()
```



#### 2. 增加数据（relationship 方法）(推荐)

##### 在`create_table_ForeignKey.py`

```python
# create_table_ForeginKey.py

  from sqlalchemy.ext.declarative import declarative_base
  from salalchemy import Column, INT, VARCHAR, ForeignKey
  from sqlalchemy import create_engine
+ from sqlalchemy.orm import relationship

  Base = declarative_base()

  class Student(Base):
    __table__ = 'student'
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(32))
    school_id = Column(INT, ForeignKey('school.id'))
+   stu2sch = relationship('School'，backref='sch2stu')

  class School(Base):
    __table__ = 'school'
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(32))


  engine = create_engine('mysql+pymysql://root:root@localhost:3306/fast_demo?charset=utf8')
  Base.metadata.create_all(engine)
```

##### 1. 正向

```python
# crud_insert_ForeignKey.py

from sqlalchemy.orm import sessionmaker
from create_table_ForeignKey import engine, School, Student

Session = sessionmaker(engine)
db_session = Session()

stu_obj = Student(name='zs', stu2sch=School(name='pekingUnivesity'))

db_session.add(stu_obj)
db_session.commit()
db_session.close()
```

##### 2. 反向

```python
# crud_insert_ForeignKey.py

from sqlalchemy.orm import sessionmaker
from create_table_ForeignKey import engine, School, Student

Session = sessionmaker(engine)
db_session = Session()

sch_obj = School(name='Tsu')
sch_obj.sch2stu = [Student(name='zhangsan'),Student(name='lisi')]

db_session.add(sch_obj)
db_session.commit()
db_session.close()
```



### 3. 多表select

#### 1. 原始查询数据（笨）

```python
# crud_select_ForeignKey.py

from sqlalchemy.orm import sessionmaker
from create_table_ForeignKey import engine，

Session = sessionmaker(engine)
db_session = Session()

# 查询
sch_obj = db_session.query(School).filter(School.name == 'pekingUniversity').first()
beijing_stu_obj = db_session.query(Student).filter(Student.school.id == sch_obj,id).first()
print(beijing_stu_obj.name,sch_obj.name)

```

#### 2. 查询数据（relationship方法）（推荐）

在`create_table_ForeginKey.py`

```python
# create_table_ForeginKey.py

  from sqlalchemy.ext.declarative import declarative_base
  from salalchemy import Column, INT, VARCHAR, ForeignKey
  from sqlalchemy import create_engine
+ from sqlalchemy.orm import relationship

  Base = declarative_base()

  class Student(Base):
    __table__ = 'student'
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(32))
    school_id = Column(INT, ForeignKey('school.id'))
+   stu2sch = relationship('School'，backref='sch2stu')

  class School(Base):
    __table__ = 'school'
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(32))


  engine = create_engine('mysql+pymysql://root:root@localhost:3306/fast_demo?charset=utf8')
  Base.metadata.create_all(engine)
```

##### 1. 正向

```python
# crud_select_ForeignKey.py

from sqlalchemy.orm import sessionmaker
from create_table_ForeignKey import engine，

Session = sessionmaker(engine)
db_session = Session()

# 查询
stu_obj = db_session.query(Student).filter(Student.name=='Tsu').first()
print(stu_obj.name, stu_obj.stu2sch.name)

```



##### 2. 反向

```python
# crud_select_ForeignKey.py

from sqlalchemy.orm import sessionmaker
from create_table_ForeignKey import engine，

Session = sessionmaker(engine)
db_session = Session()

# 查询
sch_obj_list = db_session.query(School).all()
for row in sch_obj_list:
  for stu in row.sch2stu:
    print(sch.name, stu.name)
```



### 4.多表update

```python
# crud_update_ForeignKey.py

from my_ForeignKey import Student, ClassTable,engine

from sqlalchemy.orm import sessionmaker
DB_session = sessionmaker(engine)
db_session = DB_session()

# 更新
class_info = db_session.query(School).filter(School.name=="OldBoyS1").first()

db_session.query(Student).filter(Student.id == class_info.id).update({"name":"NBDragon"})

db_session.commit()
db_session.close()

```



### 5. 多表delete

```python
# crud_delete_ForeignKey.py

from my_ForeignKey import Student, ClassTable,engine

from sqlalchemy.orm import sessionmaker
DB_session = sessionmaker(engine)
db_session = DB_session()

# 删除
class_info = db_session.query(ClassTable).filter(ClassTable.name=="OldBoyS1").first()
db_session.query(Student).filter(Student.class_id == class_info.id).delete()

db_session.commit() 
db_session.close()

```


