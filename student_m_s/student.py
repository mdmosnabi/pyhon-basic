class student:
    def __init__(self,name,roll,class_name):
            self.name = name
            self.roll = roll
            self.class_name = class_name
    def __str__(self):
        return f'{self.name},{self.roll},{self.class_name}'
    

