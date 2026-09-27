#Define the class Animal and create the objects. Recall that we have defined the class Animal as:
#Attributes: These are the data points that define an animal, such as species, name, age, habitat, and diet.
#Methods: These are the actions an animal can perform, such as make_sound(), eat(), and move().

class animal:
    def __init__(self,species,name,age,habitat,diet,direction):
                 self.species=species
                 self.name=name
                 self.age=age
                 self.habitat=habitat
                 self.diet=diet
                 self.direction=direction

    def make_sound(self):
        print(f"{self.name} is making a sound")

    def eat(self,food):
        print(f"{self.name} is eating {food}")
    
    def move(self):
       print(f"{self.name} is moving in the {self.direction} direction")

animal1=animal('dog','max',5,'house','meat','forward')

animal1.make_sound()
animal1.eat('bones')
animal1.move()