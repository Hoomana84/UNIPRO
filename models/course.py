from sqlalchemy import Column, Integer, String
from . import course as schemas
from fast1 import Base


class course(Base):
    __tablename__ = "Course"

    CID = Column(String,primary_key=True)
    CName=Column(String)
    Department=Column(String)
    Credit=Column(Integer)