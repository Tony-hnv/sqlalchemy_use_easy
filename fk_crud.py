from sqlalchemy.orm import sessionmaker
from database import engine, User, Item

Session = sessionmaker(engine)
db_session = Session()

# 添加
# 常规方法(省略不写了。。。)

# relationship添加--正向
# user_obj = User(name='理理', department='市场部', us2it=Item(name='apple', location='beijing', prince=10.0))
# db_session.add(user_obj)
# db_session.commit()
# db_session.close()

# relationship添加--反向(转换对象的数据一定要写到数组列表里，对象类型也是)
# item_obj = Item(name='samsung', location='korean', prince=29.99)
# item_obj.it2us = [User(name='花花', department='人力资源')]
# db_session.add(item_obj)
# db_session.commit()
# db_session.close()


# 查询
# 查询--常规方法(省略不写了。。。)

# relationship查询--正向
# user_obj = db_session.query(User).filter(User.name == '理理').first()
# print(user_obj.name, user_obj.us2it.name)

# relationship查询--反向(与正向同理)


# 更新
# (只有一般方法，没有relationship方法)
# user_info = db_session.query(User).filter(User.name == '理理').first()
# db_session.query(Item).filter(Item.iid == user_info.uid).update({'name': '小米'})
# db_session.commit()
# db_session.close()


# 删除
# (只有一般方法，没有relationship方法)
# user_info = db_session.query(User).filter(User.name == '理理').first()
# db_session.query(Item).filter(Item.iid == user_info.item_id).delete()
# db_session.commit()
# db_session.close()