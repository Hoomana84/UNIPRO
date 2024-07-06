# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get('/')
# def index():
#     return {'you are good std.'}
#
#
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get('/home/name/alpr/{name}')
# def index(name: str, age: int = 25):
#     return {'message': f'{name} is {age} years old!'}
# #
# from pydantic import BaseModel
# from fastapi import FastAPI
# from typing import Union
#
# app = FastAPI()
#
#
# class Person(BaseModel):
#     name: str
#     age: int
#     height: Union[int, None] = 25
#
#
# @app.post('/home/')
# def index(pss: Person):
#     return pss.age
#
#
#





































































# class Person:
#     def __init__(self, fname , lname):
#         self.fname = fname
#         self.lname = lname
#
#     @property
#     def fullname(self):
#         return f'{self.fname} {self.lname}'
#
#     @property
#     def email(self):
#         return f'{self.fname}_{self.lname}@gmail.com'
#
#
# a = Person('hooman', 'alp')
# a.fname = 'mahdi'
# print(a.fname)
# print(a.lname)
# print(a.email)
# print(a.fullname)
#
