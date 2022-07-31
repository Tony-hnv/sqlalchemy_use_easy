from fastapi import FastAPI, Depends
import hashlib
from sqlalchemy.orm import Session

from database import engine, User, Item
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)
db_session = Session()


app = FastAPI()
@app.get('/')
async def Hello_world():
  return {'msg':'Hello world!'}

@app.post('/sign_in')
async def create_user(u_name: str, u_department: str):
  try:
    db_session.add(User(name=u_name,department=u_department))
    db_session.commit()
    return '添加成功！'
  except:
    db_session.rollback()
    return '添加失败！'

@app.get('/showUserInfo')
async def showUserInfo():
  try:
    res_list = []
    user_list = db_session.query(User).all()
    for row in user_list:
      res_list.append({'id': row.uid, 'name': row.name, 'department': row.department})
    return res_list
  except:
    db_session.rollback()
    return '查询失败！'