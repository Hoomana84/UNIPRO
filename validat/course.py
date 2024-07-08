from pydantic import BaseModel, Field, validator
import json


persion_char = ["", "آ", "ا", "ب", "پ", "ت", "ت", "ث", "ج", "چ"
                                                            "ح", "خ", "د", "ذ", "ر", "ز", "ژ", "س", "ش", "ص", "ض",
                "ط", "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م", "ن", "و"
    , "ه", "ی", "ء"]

departments = ["فنی و مهندسی", "علوم پایه", "علوم انسانی", "دامپزشکی", "اقتصاد", "کشاورزی", "منابع طبیعی"]

major = ["برق", "کامپیوتر", "عمران", "مکانیک", "معدن", "شهرسازی", "صنایع", "شیمی", "مواد", "هوافضا", "معماری"]


class Course(BaseModel):
    pk: int
    cid: str = Field(max_length=5)
    cname: str = Field(max_length=25)
    department: str
    credit: int

    @validator("cid")
    def vaild_cid(self, value):
        if len(value) != 5:
            raise ValueError("This cid for this course is not valid!")
        return value

    @validator("cname")
    def vaild_cname(self, value):
        if len(value) != 25:
            raise ValueError("This name is invalid")
        if (value[:] in departments) and (value[:] in persion_char):
            raise ValueError("invalid name of course!")
        return value

    @validator("department")
    def vaild_department(self, value):
        if value not in departments:
            raise ValueError("This department is not founded!")
        return value

    @validator("credit")
    def vaild_credit(self, value):
        if not (1 <= value <= 4):
            raise ValueError("Invalid credit value!")
        return value

