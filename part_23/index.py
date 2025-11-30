# polymorphism , Encapsulatios
# x = 5 + 6
# y = '5' + '6'
# print(y)

class A:
    __x = 'data'

class B(A):
    pass

obj = B()
print(obj.__x)