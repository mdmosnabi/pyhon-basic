
# def decorator(fun):
#     print('I am decorators scope...')
#     def wraper(*a):
#         print('Before functions..')
#         x = fun(*a)
#         print('After functions...')
#         return x
#     return wraper

# @decorator
# def add(a):
#     return print(' I am a functions...',a)

# add(5)

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b

# def example(f,s):
#     return f(6,4)*s

# print(example(add,8))
# print(example(sub,8))

# x = lambda a,b: a*b

# print(x(8,7))

# def add():
#     print('I am here...')
#     return add()

# add()

def gen():
    yield 1
    yield 2
    yield 3
    yield 4

x = gen()

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
