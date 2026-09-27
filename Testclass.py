class Student:
    def __init__(self,name,student_id,major,gpa,year):
        self.name=name
        self.student_id=student_id
        self.major=major
        self.gpa=gpa
        self.year=year
        
    def enroll_course(self,course_name):
        self.course_name=course_name
        print(f'{self.name} is enrolled in {self.course_name}')
        
    def update_gpa(self,new_gpa):
        self.gpa=new_gpa
        print(f'{self.name}s new gpa is {self.gpa}')
        
    def graduate(self):
        print(f'{self.name} is graduated')
        
student1=Student('x',1,'cs','4',2026)
student2=Student('y',1,'cs','3',2024)
student1.enroll_course('electrical')
student2.update_gpa(4)
student1.graduate()