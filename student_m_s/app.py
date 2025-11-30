from manage import manager
from student import student

manager_obj = manager()

print('0. Close app')
print('1. Show all Students')
print('2. Add Student')
print('3. Search Student')
print('4. Delete Student')
print('5. Update Student')

while True:
    options = int(input('Select a options : '))
    print('===========================')
    if options == 0:
        break
    elif options == 1:
        manager_obj.show()
    elif options == 2:
        name = input('Student name : ')
        roll = input('Roll : ')
        a = manager_obj.search(roll)
        while True:
            if a == 'student not exesist':
                break
            else:
                print('Roll already exesist..')
                roll = input('Roll : ')
                a = manager_obj.search(roll)

        class_name = input('Class : ')
        manager_obj.add(student(name,roll,class_name))
        print('Add successfull..')
    elif options == 3:
        roll = input('Roll : ')
        a = manager_obj.search(roll)
        print(a)
    elif options == 4:
        roll = input('Roll : ')
        a = manager_obj.delete(roll)
        print(a)

    elif options == 5:
        roll = input('Roll : ')
        a = manager_obj.update(roll)
        print(a)