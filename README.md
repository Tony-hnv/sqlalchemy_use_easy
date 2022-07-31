# SQLAlchemy 简单快速上手
***
## 基本概念
`SQLAlchemy`是`Python`编程语言中的一个`ORM框架`，基于`数据库API`，使用`关系对象映射`进行数据库操作。

`ORM`：对象关系映射，对象和关系之间的映射，使用面向对象的方法操作数据库。

`对象关系映射orm（object relational mapping)`：通过使用描述对象和数据库之间映射的元数据，自动将面向对象语言程序中的对象持久化到关系数据库中。

> 简而言之：SQLAlchemy将对象转换成SQL，然后使用数据API执行SQL并获得执行结果。

## 安装依赖包
1. pymysql
```shell
pip install pymysql
```

2. SQLAlchemy
```shell
pip install SQLAlchemy
```

3. fastapi（若使用）
```shell
pip install fastapi
```

4. virtualenv，uvicorn（若使用）
```shell
pip install virtualenv
pip install uvicorn
```

## 该项目文件相应作用
`database.py`:
> 配置orm框架的数据库连接参数，并创建数据库连接对象。

`crud.py`:
> 实现数据库的增删改查操作。可调用也可舍弃该文件，在使用时重写crud语句

`main.py`:
> main.py是FastAPI的入口文件，实现了FastAPI的初始化、路由、接口、异常处理等功能。