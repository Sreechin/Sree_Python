### Defining Class : Classes are a fundamental concept in object-oriented programming (OOP) that allow you to create your own custom data types. 
# A class is a blueprint for creating objects, which are instances of the class. Classes can contain attributes (data) and methods (functions) that define the behavior of the objects created from the class.
#self represents the instance of the class currently being used. 
# It allows methods inside a class to access and modify that specific object's data (attributes).
class Car:
  # Initialize the Car object with make, model, year, and color
  def __init__(self, make, model, year, color):
    self.make = make  # Assign the make of the car
    self.model = model  # Assign the model of the car
    self.year = year  # Assign the year of the car
    self.color = color  # Assign the color of the car

  # Method to start the car
  # What is methid: A method is a function that is defined within a class 
  # and is associated with the objects created from that class. 
  # Methods are used to define the behavior of the objects and can access and manipulate the attributes of the class. In Python, methods are defined using the def keyword, just like regular functions, but they must have at least one parameter (usually named self) that refers to the instance of the class.
  def start(self):
    print(f'The {self.color} {self.make} {self.model} is starting.')

  # Method to stop the car
  def stop(self):
    print(f'The {self.color} {self.make} {self.model} is stopping.')

  # Method to drive the car
  def drive(self):
    print(f'The {self.color} {self.make} {self.model} is driving.')

  # Method to return a string representation of the Car object
  def __repr__(self):
    return f'I am a {self.color} {self.make} {self.model} car!'

## Creating an object of the car class

#Objects are instances of a class, and 
# they are created by calling the class as if it were a function. 
# When you create an object, the __init__ method is automatically called 
# to initialize the object's attributes.

class Car:
  # Initialize the Car object with make, model, year, and color
  def __init__(self, make, model, year, color):
    self.make = make  # Assign the make of the car
    self.model = model  # Assign the model of the car
    self.year = year  # Assign the year of the car
    self.color = color  # Assign the color of the car

  # Method to start the car
  def start(self):
    print(f'The {self.color} {self.make} {self.model} is starting.')

  # Method to stop the car
  def stop(self):
    print(f'The {self.color} {self.make} {self.model} is stopping.')

  # Method to drive the car
  def drive(self):
    print(f'The {self.color} {self.make} {self.model} is driving.')

  # Method to return a string representation of the Car object
  def __repr__(self):
    return f'I am a {self.color} {self.make} {self.model} car!'

car1 = Car("Toyota", "Camry", 2020, "red")
car1

car2 = Car("Honda", "Civic", 2019, "blue")
car2

car3 = Car("Ford", "Mustang", 2021, "black")
car3

car1.start()
car2.drive()
car3.stop()