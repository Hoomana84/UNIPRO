# # f = open('test.txt','r')
# #
# #
# # print(f.read())
# #
# # f.close()
#
# with open('test.txt', 'r') as f:
#
#     print(f.read(7))
#     print(f.read(7))
#
#     f.seek(18)
#
#     print(f.tell)
#
#
# name = 'jack'
# age = 34
#
# print(name + 'is' + str(age) + 'years old.')
# print()
# print(f'{name} is {age} years old')
# print()
# print(f'{name:10} is {age:8} years old')
# print()
# print('{n} is {a} years old'.format(n=name, a=age))
# print()
# info = {'name': 'jack', 'age': 34}
# info2 = {'name': 'anna', 'age': 41}
# print('{0[name]} is {0[age]}years old and {1[name]} is {1[age]}years old.'.format(info, info2))
