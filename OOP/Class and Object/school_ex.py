class Student:
    def __init__(self, name, course, id):
        self.name = name
        self.course = course
        self.id = id

    def __repr__(self) -> str:
        return f'Student: {self.name}, Course: {self.course}, ID: {self.id}'
    
class Teacher: 
    def __init__(self, name, sub, id):
        self.name = name
        self.sub = sub
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher: {self.name}, Subject: {self.sub}, ID: {self.id}'

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_teacher(self, name, sub):
        id = len(self.teachers) + 220
        teacher = Teacher(name, sub, id)
        self.teachers.append(teacher)

    def add_stu(self, name, fee):
        if fee<6000:
            return f'Not enough fee.'
        else:
            id = len(self.students) + 309
            student = Student(name,'c', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}'
        
    def __repr__(self) -> str:
        print("Welcome to", self.name)
        print("-----> Our Teachers <-----")
        for teacher in self.teachers:
            print(teacher)
        print("-----> Our Students <-----")
        for student in self.students: 
            print(student)

        return 'All Done.'
    

pu = School("Presidency University")

pu.add_stu('Alia', 5800)
pu.add_stu('Karina', 6700)
pu.add_stu('Selmon', 6000)

pu.add_teacher('Tom', 'DS')
pu.add_teacher('Halland', 'OPP')

print(pu)