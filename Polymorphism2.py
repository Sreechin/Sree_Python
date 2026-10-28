#Grandparent: Has a method speak().
#Parent: Inherits from Grandparent and overrides speak().
#Child: Inherits from Parent and overrides speak().
#Grandchild: Inherits from Child and overrides speak().

class Grandparent:
    def speak(self):
        print("I'm Grandparent.Give me someting to eat")

class Parent(Grandparent):
    def speak(self):
        print("I'm Parent.Give some food to genadpa")

class Child(Parent):
    def speak(self):
        print("I'm Child.Give some food")

class GrandChild(Child):
    def speak(self):
        print("I'm Grandchild.Give some food")

Grandparent=Grandparent()
Parent=Parent()
Child=Child()
GrandChild=GrandChild()


for person in (Grandparent,Parent,Child,GrandChild):
  person.speak()
