#  self parameters 

class A:
    x = 'sasd'
    def fun1(my_obj):
        return 'Mosnabi'
    def fun2(self):
        return self.fun1()+'data'
    
obj = A()
print(obj.fun1())