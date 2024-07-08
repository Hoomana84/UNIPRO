from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class student(BaseModel):
    stid: str
    fname: str
    lname : str
    father : str


class Config:
    orm_mode = True


class prstu(student):
    birth: str
    ids: str 
    borncity: str
    address: str
    postalcode: str
    cphone: str
    hphone: str     
    department: str
    major: str   
    married: str
    id: str
    scourseids: str
    lids:  str  


class studentupdate(BaseModel):
    stid:str
    fname: str
    lname: str
    father:str
    birth:str
    ids:str 
    birncity: str 
    address:str 
    postalcode:str 
    cphone: str 
    hphone: str 
    department: str 
    major: str 
    married:str 
    id: str 
    scpirseids:str 
    lids: str 
