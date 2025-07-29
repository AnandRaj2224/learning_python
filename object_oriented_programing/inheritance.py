class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self,sound):
        print(f"this animal make {sound}\n")

class Cat(Animal): # pass the parent class in the child class
    def __init__(self, name,breed,fav_toy,species = "felis catus"):
        super().__init__(name, species)
        self.breed = breed
        self.fav_toy = fav_toy
    def __repr__(self):
        return f"this cat called {self.name} is a {self.breed} of species {self.species} and his fav toy is {self.fav_toy} "

cat = Cat("slayer of mice","bombay_cat","soul of its deafeated enemies")
print(cat)
'''
Animal 
        name
        species
cat     
        name
        species
        breed
        fav_toy
'''

# multiple inheritance
# syntax  ----> class Cat(Animal,Mammal,etc)