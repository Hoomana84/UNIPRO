

from sqlalchemy import Column, Integer, String
from fast1.database import Base


class Teacher(Base):

    __tablename__ = "Teachers"
    pk = Column(Integer, primary_key=True, unique=True)
    LID = Column(Integer, primary_key=True, unique=True)
    fname = Column(String)
    Lname = Column(String)
    ID = Column(Integer, unique=True)
    department = Column(String)
    major = Column(String)
    birth = Column(Integer)
    borncity = Column(String)
    address = Column(String)
    postalcode = Column(String)
    cphone = Column(Integer)
    hphone = Column(Integer)
    LCourseIDs = Column(Integer)
