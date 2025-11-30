# x = 0
# if x == 0:
#     if 4>3:
#         pass
#     print(' yes it is ok')
# elif x > 0:
#     print('x gatter then 0')
# # elif x < 0:
# #     print(' x lass then 0')

# else :
#     print('default')
# if x:
#     print(x)

# x = 'asdasd' if 4>5 else 0
# print(x)
# if 4>3 : print('ok')

x = 8
match x:
    case 5|8:
        print(' x is 5')
    case 3:
        print('x is 3')
    case _:
        print(' unknown')
