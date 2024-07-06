# class Car:
#     def __init__(self, n, p, c):
#         self.name = n
#         self.price = p
#         self.color = c
#         print(f'{self.name} costs {self.price}! and it\'s color is {self.color}.')
#
#
# c1 = Car('Pride', '350', 'red')
# c2 = Car('Benz', '980', 'blue')






class Car:
    wheel = 4

    def __init__(self, n, p):
        self.name = n
        self.price = p

    def show_wheel(self):
        print(f'{self.name} costs {self.price}  and it has {self.wheel}.')


c1 = Car('Pride', 350)
c2 = Car('Benz', 986)

c1.wheel = 5

c1.show_wheel()
c2.show_wheel()









































# # class Car:
# #     pass
# #
# #
# # a = Car()
# # b = Car()
# #
# # a.name = 'Pride'
# # b.name = 'Benz'
# #
# # a.price = 100
# # b.price = 900
# # print(f'{a.name} is {a.price} and {b.name} is {b.price}.!')
