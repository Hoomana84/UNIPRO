from pydantic import BaseModel, Field, validator
import json

class Teacher(BaseModel):
    pk: int
    LID: int = Field(max_length=6)
    fname: str
    lname: str
    ID: int
    department: str
    major: str
    birth: int
    borncity: str
    address: str = Field(max_length=100)
    postalcode: str = Field(max_length=10)
    cphone: int
    hphone: int
    LCourseIDs: int


@validator("LID")
def vaild_LID(self, value):
    if len(value) != 6:
        raise ValueError("Invalid LID value!")
    return value


@validator("fname")
def vaild_fname(self, value):
    for i in value:
        if i not in persion_char:
            raise ValueError("fname is not correct!")
    if len(value) != 10:
        raise ValueError("Invalid fname!")
    return value


@validator("lname")
def vaild_lname(self, value):
    if len(value) != 10:
        raise ValueError("This lname is not too long")
    for i in value:
        if i not in persion_char:
            raise ValueError("please using persion character only!")
    return value


@validator("ID")
def vaild_ID(self, value):
    value = str(value)
    if not len(value) == 10:
        raise ValueError("national code is not correct!")

    res = 0
    for i, num in enumerate(value[:-1]):
        res += int(num) * (10 - i)
    remain = res % 11
    if remain < 2:
        if not remain == int(value[-1]):
            raise ValueError("natinal code is not correct!")
        return value


@validator("department")
def vaild_department(self, value):
    if value not in departments:
        raise ValueError("department is not correct!")
    return value


@validator("major")
def vaild_major(self, value):
    if value not in major:
        raise ValueError("major is not correct!")
    return value


@validator("birth")
def vaild_birth(self, value):
    if len(value) > 10 or len(value[4]) != "-" or value[7] != "-":
        raise ValueError("format is not correct!")
    list = value.split("-")
    year = int(list[0])
    if not 1403 > year > 1300:
        raise ValueError("year is not good!")
    month = int(list[1])
    if not 1 <= month <= 12:
        raise ValueError("month is not good")
    day = int(list[2])
    if not 1 <= day <= 31:
        raise ValueError("day is not good!")
    return value


@validator("borncity")
def vaild_borncity(self, value):
    with open('unit\data\cities.json', 'r', encoding="utf-8") as file:
        cities = json.load(file)
        cities = list(cities)
        new_cities = []
        for c in cities:
            new_cities.append(c["name"])

    if value not in new_cities:
        raise ValueError("city is not correct!")
    return value


@validator("address")
def vaild_address(self, value):
    if len(value) != 100:
        raise ValueError("This address  have wrong!")
    return value


@validator("postalcode")
def vaild_postalcode(self, value):
    if len(value) != 10:
        raise ValueError("Invalid code!")
    return value