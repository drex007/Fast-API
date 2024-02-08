from bson import ObjectId
from fastapi import APIRouter

from models.user import User
from database import connection
from schemas.user import usersEntity, userEntity

user = APIRouter()

@user.get('/users')
async def get_all():
  return usersEntity(connection.local.user.find())

@user.get('/users/{id}')
async def get_user(id):
  return userEntity(connection.local.user.find_one({'_id':ObjectId(id)}))


@user.post('/create-user')
async def create_user(user: User):
  connection.local.user.insert_one(dict(user))
  return usersEntity(connection.local.user.find())

@user.put('/update-user/{id}')
async def update_user(id, user:User):
  connection.local.user.find_one_and_update({"_id": ObjectId(id)},{
    '$set': dict(user)
  } )
  return userEntity(connection.local.user.find_one({'_id': ObjectId(id)}))


@user.delete('/delete-user/{id}')
async def delete_user(id):
  return userEntity(connection.local.user.find_one_and_delete({'_id': ObjectId(id)}))

