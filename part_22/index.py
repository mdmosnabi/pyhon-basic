# python inheritance 

class A: # super class
    def __init__(self,a,b):
        self.a = a 
        self.b = b
    x = 'I am x'

class B(A): # sub class
    def __init__(self, a, b):
        super().__init__(a, b)
    y = 'I am y'



obj_b = B(4,5)
print(obj_b.a)



# class A:
#     x = 'I am x'

# class B:
#     y = 'I am y'

# class C:
#     z = 'I am z'

# class hibrid(A,B,C):
#     def name(self):
#         return print(self.y)
    
# obj = hibrid()
# obj.name()