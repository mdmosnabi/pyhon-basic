# my_data , your_data = "data" ,"data 1"
# print(my_data ,your_data)

# data1 = data2 = data3 = " Name : python"

# print(data3)

# x =  'this is global '

# def name():
#     x = 'this is local'
#     return print(x)

# name()

# print(x)

def name():
    global data 
    data = "python"
    return print(data)

name()

print(data)