from typing import List, Any

from database import engine, User, Item
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)
db_session = Session()

# 添加
# ad1 = User(department='market')
# db_session.add(ad1)
# db_session.commit()
# db_session.close()

# 查询
# user_obj_list: list[Any] = db_session.query(User).all()
# print(user_obj_list)
# for row in user_obj_list:
#   print(row.uid, row.name, row.department)

# 更新
# user_update_user1 = db_session.query(User).filter(User.name == 'zhangsan').update({'department':'人力资源'})
# user_update_user2 = db_session.query(User).filter(User.department == '市场部').update({'name':'lisi'})
# db_session.commit()
# db_session.close()

# 删除
# res = db_session.query(User).filter(User.uid == 1).delete()
# db_session.commit()
# print(res)