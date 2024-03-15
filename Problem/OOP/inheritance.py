# Base class
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass

# Derived class inheriting from Animal
class Dog(Animal):
    def __init__(self, name):
        # Call the constructor of the superclass
        super().__init__('Dog')
        self.name = name

    def make_sound(self):
        return "Woof!"

# Derived class inheriting from Animal
class Cat(Animal):
    def __init__(self, name):
        # Call the constructor of the superclass
        super().__init__('Cat')
        self.name = name

    def make_sound(self):
        return "Meow!"

# Creating instances of subclasses
dog = Dog('Buddy')
cat = Cat('Whiskers')

# Accessing attributes and methods inherited from Animal
print(f"{dog.name} is a {dog.species} that makes the sound '{dog.make_sound()}'")
print(f"{cat.name} is a {cat.species} that makes the sound '{cat.make_sound()}'")
