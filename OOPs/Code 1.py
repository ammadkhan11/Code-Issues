class Animal:
    def __init__(self, name, species):
        self.name=name
        self.species=species

class Dog(Animal):
    def __init__(self,name, species, breed):
        super().__init__(name,species)
        self.breed=breed

dog1=Dog("Bono", "Pug", "Husky")
print(dog1.name)
print(dog1.species)
print(dog1.breed)