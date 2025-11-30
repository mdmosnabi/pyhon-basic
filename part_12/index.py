#  ================= Dictionary ===================

x = {
    'key':10,
    'key1':'sdasd',
    'key3':None,
}
y ={
    'name':'mosnabi',
    'array':[1,2,1,1,5]
}

# print(type(x))
# print(x['key'])
# print(x.get('key1'))
# print(x.items())
# print(x.keys())
# print(x.values())


# x['key4'] = "my"
# x.update(y)
# print(x)

# del x
# x.clear()
# x.popitem()
x.pop('key1')
print(x)
