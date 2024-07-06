# from fastapi import FastAPI, Path, Query
# from pydantic import BaseModel
# from typing import Union
#
# app = FastAPI()
#
#
# class Person(BaseModel):
#     name: str
#     age: int = Path(ge=0, le=100, title='user age')
#     height: Union[int, None] = 150
#
#
# @app.post('/home/')
# def index(pss: Person, car: str = Query('Nothing', min_length=2, max_length=30)):
#     return pss.age

#
# from fastapi import FastAPI, HTTPException, status
# from pydantic import BaseModel
# #
# app = FastAPI()
#
#
# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: str
#
#
# class UserOut(BaseModel):
#     username: str
#     email: str
#
#
# @app.post("/home/user/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
# def index(user: UserIn):
#     if user.username == "admin":
#         raise HTTPException(detail='username can\'t be admin', status_code=status.HTTP_400_BAD_REQUEST,
#                             headers={'X-Error': 'There goes my error'})
#     return user
#
#

