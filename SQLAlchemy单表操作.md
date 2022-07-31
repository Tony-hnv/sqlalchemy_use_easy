# SQLAlchemy——创建表

```python
# ORM
# 1. Class - Obj
# 2. 创建数据库引擎
# 3. 将所有的Class序列化为数据表
# 4. ORM操作 - CRUD(增删改查操作的简称)
```

## 1.创建一个 Class

```python
# create_table.py

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# Base 是ORM模型的基类
# ORM模型 - Obj里面的属性 == table中创建的字段

from sqlalchemy import Column, Integer, INT, INTEGER, VARCHAR, String
# 以上的基本数据类型和对象封装类型都是可以使用的，看个人喜好

class User(Base):
	__tablename__ = 'user' // user是即将创建的数据表名称
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(32), index=True)
```

## 2. 创建数据引擎
```python
# create_table.py

from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:root@localhost:3306/fast_demo?charset=utf8')
# 'mysql+sqlalchemy://用户名:密码@数据库主机地址:端口号/数据库名?字符编码格式（可选）'
# ?字符编码格式（可选）
# 如果存储内容中文，建议设置charset = utf8
```

## 3. 将所有的继承Base的Class序列化成数据表
```python
# create_table.py

Base.meatdata.create_all(engine)
# 在基类中寻找所有继承自我的Class，在engine里实现
```



# SQLAlchemy——增

```python
# 1. 选中数据库 - 创建数据库引擎 导入数据库引擎
# 2. 创建查询窗口 - 必须是选中数据的查询窗口
# 3. 创建sql语句
# 4. 点击运行
```

- 增加一条数据

> `原生SQL语句`:
> `insert into '表名'(name) values (值1, 值2, ...)`

```python
# crud_insert.py

# 1. 选中数据库 - 创建数据库引擎 导入数据库引擎
from create_table import engine

# 2. 创建查询窗口 - 必须是选中数据的查询窗口
from sqlalchemy.orm import sessionmaker
Session_windew = sessionmaker(engine)

# 打开查询窗口
db_session = Session_window()

# 3. 创建sql语句
from create_table import User
user_obj = User(name='aabbcc') # 创建sql语句
db_session.add(user_obj) # 相当于将sql语句粘贴到查询窗口
db_session.commit() # 执行sql语句
db_session.close() # 关闭

```

- 增加多条数据

```python
from create_table import User
user_obj_list = ['User(name='zs'), User(name='lisi')']
db_session.add_all(user_obj_list)
db_session.commit()
db_session.close()
```



# SQLAlchemy——查

- 查询数据

> `原生SQL语句`:
> `sellect 字段[,字段一，字段二，...] from 表名 [其他操作]`

```python
# crud_select.py

from create_table import engine， User
from sqlalchemy.orm import sessionmaker

# 创建查询窗口
Session = sessionmaker(engine)
db_session = Session()

# 1.查询数据:
user_obj = db_session.query(User).first()
print(user_obj.id, user_obj.name)

user_obj_list = db_session.query(User).all()
print(user_obj_list)
for row in user_obj_list：
	print(row.id, row.name)
  
# 2.带条件的查询
# filter(表达式)
user_obj1 = db_session.query(User).filter(User.id <=2,User.name == 'zs').all()
print(user_obj1)
for row in user_obj1：
	print(row.id, row.name)
  
# filter(表达式)
# filter_by(传参)，不推荐使用，不方便
user_obj1 = db_session.query(User).filter(User.id =2,User.name = 'zs').all()
print(user_obj1)
for row in user_obj1：
	print(row.id, row.name)

```



# SQLAlchemy——改

- 更新数据

> `原生SQL语句`:
>
> `update 表名 set 字段名=“value”, ...`

```python
# crud_update.py

from sqlalchemy.orm import sessionmaker
from create_table import engine,User

# 创建查询窗口
Session = sessionmaker(engine)
db_session = Session()

# 1. 修改一条数据
user_obj = db_session.query(User).filter(User.id == 1).update({"name":"ww"})
db_session.commit()

# 2. 修改多条数据
user_obj = db_session.query(User).filter(User.id >= 1).update({"name":"666"})
db_session.commit()


```



# SQLAlchemy——删

- 删除数据

> `原生SQL语句`:
>
> `delete from 表名 [筛选条件]`——此命令只会删除表内数据，不会删除表
>
> `drop 表名`——此命令会直接删除表本身

```python
# crud_delete.py

from sqlalchemy.orm import sessionmaker
from create_table import engine,User

# 创建查询窗口
Session = sessionmaker(engine)
db_session = Session()

# 删除一条数据
res = db_session.query(User).filter(User.id==1).delete()
db_session.commit()
print(res)

# 删除多条数据
res = db_session.query(User).filter(User.id>=1).delete()
db_session.commit()
print(res)

```



