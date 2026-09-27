## Defining class
class employee:

    def __init__(self, name, employee_id, department, salary):
        self.name=name
        self.employee_id=employee_id
        self.department=department
        self.salary=salary

#Defining Method

#Employee gets promoted, move to different department, get a raise

    def promote(self):
        print(f"employee {self.name} got promoted")

    def transfer(self, new_department):
        self.department = new_department
        print(f"employee {self.name} transferred to {new_department}")

    def raise_salary(self, amount):
        self.salary += amount
        print(f"employee {self.name} new salary is {self.salary}")


emp1=employee("John Doe", 12345, "IT", 50000)
emp1.promote()
emp2=employee("Jane Smith", 67890, "HR", 60000)
emp2.transfer("Finance")
emp3=employee("Alice Johnson", 54321, "Marketing", 55000)
emp3.raise_salary(5000)