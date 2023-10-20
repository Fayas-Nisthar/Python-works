class Student:
    rol:int
    course:int
    total:int
    def __init__(self,rollno,course,total):
        self.rol=rollno
        self.course=course
        self.total=total
    def display(self):
        print(self.rol,self.course,self.total)
obj1=Student(10,"django",450)
obj1.display()