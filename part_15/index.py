# ===================== Python Module ========================
# import my_module as my
# from my_module import name , x

# my_module = 'asddasda'
 
# name('mosnabi')
# print(x)

from datetime import date ,time ,datetime ,timedelta

x = '06-11-25'

y = datetime.strptime(x,'%d-%m-%y')
now = datetime.now()

print( y > now)
# print(now.strftime('%d-%m-%y %H:%S:%M'))
