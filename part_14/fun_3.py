# def add(a=0,b=0):
#     return print(f'a is:{a} b is :{b}')

# add()

# x = 'I am global..'

# def demo():
#     # global x
#     x="I am in a functions.."
#     def nested():
#         nonlocal x
#         x= 'I am nested..'
#         print(x)
#         return x
#     nested()
#     return print(x)

# demo()
# print(x)

# def demo():
#     return print('asdasd')

# x = demo
# x()

def name():
    print('addasdas')
    def nested():
        return 100
    return nested

x= name()

print(x())
