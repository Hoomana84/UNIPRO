from pydantic import BaseModel
from typing import Optional


class teacher(BaseModel):
    lid: str
    fname: str
    lname: str
    id: str


class Config:
    orm_mode = True


class pmaster(teacher):
    department: str
    major: str
    birth: str
    borncity: str
    address: str
    postalcode: str
    cphone: str
    hphone: str
    lcourseids: str


class teacherupdate(BaseModel):
    lid: str 
    fname:str 
    lname: str
    id: str 
    department: str 
    major: str 
    birth:str
    borncity:str
    address:str 
    postalcode: str 
    cphone: str 
    hphone: str 
    lcourseids:str


def prstu():
    return None


def student():
    return None
