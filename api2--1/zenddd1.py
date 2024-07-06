# def __show():
#     print('This show method is private')
#
#
# class Person:
#     name = 'hooman'
#     _age = 19
#     __height = 172
#
#     def _Person__show(self):
#         pass
#
#
# class Male(Person):
#     pass
#
#
# P = Person()
#
# P._Person__show()
#













































# import datetime
#
#
# class Person:
#     def __init__(self, name, height, age):
#         self.name = name
#         self.height = height
#         self.age = age
#
#     def show(self):
#         print(f'{self.name} is {self.height}  cm , is {self.age} years old.')
#
#     @classmethod
#     def from_brith(cls, name, height, age):
#         return cls(name, height, datetime.datetime.now().year - age)
#
#     @staticmethod
#     def is_adult(age):
#         if age >= 18:
#             print('Yes')
#         else:
#             print('NO')
#
#
# P1 = Person.from_brith('hooman', '172', 2005)
#
# P1.show()
#
# print()
#
# P1.is_adult(19)
