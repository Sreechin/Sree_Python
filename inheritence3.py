# Create two subclasses, Car and Truck, 
# each with an additional attribute: 
# number_of_doors for Car and cargo_capacity for Truck.
# Create a Vehicle object vehicle.
# Create a Car object car.
# Create a Truck object truck.
# Print the details of each object.

class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
class Car(Vehicle):
    def __init__(self,make,model,number_of_doors):
        super().__init__(make,model)
        self.number_of_doors=number_of_doors
class Truck(Vehicle):
    def __init__(self,make,model,cargo_capacity):
        super().__init__(make,model)
        self.cargo_capacity=cargo_capacity

v=Vehicle(2016,"Model Y")
print({v.model},{v.make})
c=Car(2016,"Model Z","4 doors")
print({c.model},{c.make},{c.number_of_doors})
t=Truck(2017,"Model P","200lb")
print({t.model},{t.make},{t.cargo_capacity})





