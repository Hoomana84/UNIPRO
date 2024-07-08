from pydantic import BaseModel, Field, validator
import json


persion_char = ["", "آ", "ا", "ب", "پ", "ت", "ت", "ث", "ج", "چ"
                                                            "ح", "خ", "د", "ذ", "ر", "ز", "ژ", "س", "ش", "ص", "ض",
                "ط", "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م", "ن", "و"
    , "ه", "ی", "ء"]

departments = ["فنی و مهندسی", "علوم پایه", "علوم انسانی", "دامپزشکی", "اقتصاد", "کشاورزی", "منابع طبیعی"]

major = ["برق", "کامپیوتر", "عمران", "مکانیک", "معدن", "شهرسازی", "صنایع", "شیمی", "مواد", "هوافضا", "معماری"]


class Student(BaseModel):
    pk: int
    STID: int
    fname: str
    Lname: str
    father: str
    birth: str
    IDS: str
    borncity: str
    address: str = Field(max_length=100)
    postalcode: str = Field(pattern=r"^[0-9]{10}$")
    cphone: str = Field(pattern=r"^((\+98|0|098)9\d{9})$")
    hphone: str = Field(pattern=r"^0[1|3|4|5|6|7|8|9][0-9]{9}$|^02[0-9]{9}$")
    department: str
    major: str
    married: bool
    ID: int

    # SCourseIDs: list[Lesson] = []
    # LIDs: list[Professor] = []

    @validator("STID")
    def vaild_STID(self, value):
        if len(str(value)) != 11:
            raise ValueError("student code should be 11 digits!")
        year = int(str(value)[:3])
        if not 400 <= year <= 403:
            raise ValueError("year part is not correct!")
        middle = int(str(value)[3:9])
        if middle != 114150:
            raise ValueError("middle part is not correct!")
        index = int(str(value)[-2:])
        if not 1 <= index <= 99:
            raise ValueError("index part is not correct!")
        return value

    @validator("fname")
    def vaild_fname(self, value):
        if len(value) > 10:
            raise ValueError(" this name must be less than 10 characters!")
        for i in value:
            if i not in persion_char:
                raise ValueError("Only contains persion characters!")
        return value

    @validator("lname")
    def vaild_Lname(self, value):
        if len(value) > 10:
            raise ValueError("must be less than 10 characters!")
        for i in value:
            if i not in persion_char:
                raise ValueError("Only contains persion characters!")
            return value

    @validator("father")
    def vaild_father(self, value):
        if len(value) > 10:
            raise ValueError("must be less than 10 characters!!")
        for i in value:
            if i not in persion_char:
                raise ValueError("Only contains persion characters!!")
            return value

    @validator("birth")
    def vaild_birth(self, value):
        if len(value) > 10 or len(value[4]) != "-" or value[7] != "-":
            raise ValueError("format not correct!")
        list = value.split("-")
        year = int(list[0])
        if not 1403 > year > 1300:
            raise ValueError("year not correct!")
        month = int(list[1])
        if not 1 <= month <= 12:
            raise ValueError("month not correct")
        day = int(list[2])
        if not 1 <= day <= 31:
            raise ValueError("day not correct!")
        return value

    @validator("IDS")
    def vaild_IDS(self, value):
        if (len(value) != 10) or (value[0] not in persion_char) or (value[3] != "/"):
            raise ValueError("Format of serial is not good!!")
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
            raise ValueError("city not correct!")

        return value

    @validator("department")
    def vaild_department(self, value):
        if value not in departments:
            raise ValueError("department is not good!")
        return value

    @validator("major")
    def vaildate_major(self, value):
        if value not in major:
            raise ValueError("major is found!")
        return value

    @validator("married")
    def vaildate_married(self, value):
        if value:
            return f"{value} is married"
        else:
            return f"{value} is not married"

    @validator("ID")
    def vaild_ID(self, value):
        value = str(value)
        if not len(value) == 10:
            raise ValueError("Code is not correct!")
        res = 0
        for i, num in enumerate(value[:-1]):
            res += int(num) * (10 - i)
        remain = res % 11
        if remain < 2:
            if not remain == int(value[-1]):
                raise ValueError("natinal code is not correct!")
            return value

