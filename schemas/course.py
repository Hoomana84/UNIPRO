from pydantic import BaseModel

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class Course(BaseModel):
    CID: str
    CName: str
    Department: str
    Credit: int


class CourseUpdate(BaseModel):
    CID:str
    CName: str
    Department: str
    Credit:str


def course():
    return None


def courseUpdate():
    return None