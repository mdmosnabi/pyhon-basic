
class A:
    x = 'asdasd'
    def __init__(self,a,b):
        self.a = a 
        self.b = b

    def add(self,a,b):
        return a+b

obj1 = A(4,5)
obj2 = A('as',5)
obj3 = A(4,500)

obj1.x = 'my name is x'
# del obj3.add

obj1.name = 'mosnabi'
print(obj1.x)
print(obj2.x)
# print(obj3.a,obj3.x ,obj2.add(6,4))