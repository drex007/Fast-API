from typing import Optional
from fastapi import FastAPI
from schemas.blog.blogSchema import Blog
from routes.user import user

app = FastAPI()
app.include_router(user)




  

@app.get('/')
def index():
  return {'data':f'returns all blogs'}

# @app.get('/')
# def limit(limit):
#   return {'data':f'returns {limit} blogs'}


@app.get('/all-blogs')
def limit(limit=10, published: Optional[bool] = False, sort: Optional[str]= None): # Shows Optional, default and compulsory params declarations
  if published:
    return {'data':f'returns {limit} blogs'}
  return  {'data':f'returns all db blogs'}


@app.get('/about')
def about():
  return {'data':'returns about page'}


@app.get('/blog/unpublished')
def unpublishedBlogs(): #Comementa
  try:
    return {'data':f'returns single log with ID'}
  except Exception as e:
    print("Error", e)
    return {"data": f"Error {e}"}
    


@app.get('/blog/{id}')
def getBlog(id:int):
  try:
    return {'data':f'returns single log with ID, {id}'}
  except Exception as e:
    print("Error", e)
    return {"data": f"Error {e}"}
    


@app.post('/create')
def create(payload:Blog):
  print(payload)
  return {"data":"Blog was created"}