#  python magic methods 

# class A:
#     def __init__(self,a,b):
#         self.a = a 
#         self.b = b
#     def __str__(self):
#         return 'This is class A'
#     def __len__(self):
#         return 5
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.a <= self.b:
#             self.a += 1
#             return self.a
#         else:
#             raise StopIteration
#     def __call__(self, *args, **kwds):
#         return 200
    
        

# obj = A(5,7)

# print(obj())

# for i in obj:
#     print(i)

class A:
    def __init__(self,list):
        self.list = list

    def __contains__(self,item):
        return item in self.list
    
obj = A([2,5,6,7,8,10,15,4])
print(5 in obj)