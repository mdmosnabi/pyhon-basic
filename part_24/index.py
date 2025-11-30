#  overriding
class A:
    def name(self):
        return 'I am methods of A'
    
class B(A):
    def name(self):
        return 'I am methods of B'

obj = B()
print(obj.name())