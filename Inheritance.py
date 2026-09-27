#Inheritance is a key concept in object-oriented programming (OOP). 
# It allows one class (called the child class or subclass) to 
# inherit attributes and methods from another class (called the 
# parent class or superclass). 
# This promotes code reuse, enables a hierarchical structure, 
# and simplifies code maintenance.

#Parent Class (Superclass): The base class that provides attributes and methods to its subclasses.
#Child Class (Subclass): A class that inherits from a parent class and can have additional attributes or methods.
#super(): A function that allows access to the parent class’s methods or attributes, often used to call the parent class constructor (__init__()).

class A:
    def __init__(self,attr1,attr2):
        self.attr1=attr1
        self.attr2=attr2

    def act(self):
        print("This method is of class A")
class B(A):
    def __init__(self,attr1,attr2,attr3):
        super().__init__(attr1,attr2)
        self.attr3=attr3
class C(A):
    def __init__(self,attr1,attr2,attr4):
        super().__init__(attr1,attr2)
        self.attr4=attr4

class D(C):
    def __init__(self,attr1,attr2,attr4,attr5):
        super().__init__(attr1,attr2,attr4)
        self.attr5=attr5

a = A('Class A', 'SuperClass')
print(a.attr1, a.attr2)
a.act()

b = B('Class B', 'subclass','Mat')
print(b.attr1, b.attr2, b.attr3)
b.act()

c = C('Class B', 'subclass', 'Bat')
print(c.attr1, c.attr2, c.attr4)
c.act()

d = D('Class B', 'subclass', 'Bat')
print(b.attr1, b.attr2, b.attr5)
b.act()

