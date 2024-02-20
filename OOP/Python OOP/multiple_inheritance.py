class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Flyable:
    def fly(self):
        print(f"{self.name} is flying")

class Bird(Animal, Flyable):
    def __init__(self, name, species):
        # Multiple inheritance: calling constructors of both base classes
        Animal.__init__(self, name)
        Flyable.__init__(self)
        self.species = species

    def display_info(self):
        print(f"{self.name} is a {self.species} bird")

# Usage
parrot = Bird("Polly", "Parrot")

parrot.display_info()
parrot.eat()          
parrot.fly()          
