from student import student

class manager:
    FILE_NAME = 'student.txt'

    def __init__(self):
        self.student_list = []
        self.load()

    def load(self):
        try:
            with open(self.FILE_NAME,'r') as file:
                for line in file:
                    name,roll,class_name = line.strip().split(',')
                    a=student(name,roll,class_name)
                    self.student_list.append(a)
        except Exception as e :
            print(e)
    
    def show(self):
        for item in self.student_list:
            print(str(item))

    def search(self,roll):
        for i in self.student_list:
            if i.roll == roll:
                return i
        return "student not exesist"
    
    def delete(self,roll):
        a = self.search(roll)
        if a=='student not exesist':
            return a
        self.student_list.remove(a)
        with open(self.FILE_NAME,'w') as file:
            for item in self.student_list:
                file.write(f'{item}\n')
        return 'Delete successfull'

    def add(self,student_obj):
        self.student_list.append(student_obj)
        with open(self.FILE_NAME,'a') as file:
            file.write(f'{student_obj}\n')
    def update(self,roll):
        a = self.search(roll)
        if a=='student not exesist':
            return a
        self.student_list.remove(a)
        name = input("Student's name : ")
        class_name = input("Student's Class : ")
        self.student_list.append(student(name,roll,class_name))
        with open(self.FILE_NAME,'w') as file:
            for item in self.student_list:
                file.write(f'{item}\n')
        return 'Update Successfull'