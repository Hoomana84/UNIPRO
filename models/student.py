
from sqlalchemy import Boolean,Column, Integer, String
from fast1.database import Base


class Student(Base):

    __tablename__ = "students"
    pk = Column(Integer, primary_key=True, unique=True)
    STID = Column(Integer, unique=True)
    fname = Column(String)
    Lname = Column(String)
    father = Column(String)
    birth = Column(String)
    IDS = Column(String)
    borncity = Column(String)
    address = Column(String)
    postalcode = Column(String)
    cphone = Column(String)
    hphone = Column(String)
    department = Column(String)
    major = Column(String)
    married = Column(Boolean)
    ID = Column(Integer, unique=True)
    SCourseIDs = Column(Integer)
    LIDs = Column(Integer)


def student():
    return pass