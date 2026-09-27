class Animal:
    def __init__(self,species,diet):
        self.species=species
        self.diet=diet
class Mammal(Animal):
    def __init__(self,species,diet,fur_color):
        super().__init__(species,diet)
        self.fur_color=fur_color
class Bird(Animal):
    def __init__(self,species,diet,wing_span):
        super().__init__(species,diet)
        self.wing_span=wing_span

a=Animal("fox","meat")
print({a.species},{a.diet})

b=Mammal("fox","meat","brown")
print({b.species},{b.diet},{b.fur_color})

c=Bird("Pigeon","seeds","2 ft")
print({c.species},{c.diet},{c.wing_span})