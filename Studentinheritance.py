class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class student(person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id

p1=person('abby',10)
print(f"The person name is {p1.name} and she is {p1.age} old")

s1=student('abby',10,1234)
print(f"The person name is {s1.name},age {s1.age}. Her Student id is {s1.student_id}")
