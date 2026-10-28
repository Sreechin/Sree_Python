# polymorphism allows you to define methods in a base class 
# and have those methods be overridden by subclasses to 
# provide specific behavior.

class Animal:
    def speak(self):
        print("Make some sound and I don't know what that sound is like..")

class Cat(Animal):
    def speak(self):
        print("meo")

class Dog(Animal):
    def speak(self):
        print("bow")

a=Animal()
b=Cat()
c=Dog()

a.speak()
b.speak()
c.speak()