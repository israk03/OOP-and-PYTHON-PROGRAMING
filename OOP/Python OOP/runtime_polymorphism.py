class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

# Function to demonstrate polymorphism
def animal_sounds(animal):
    animal.make_sound()

# Usage
animal1 = Dog()
animal2 = Cat()

animal_sounds(animal1)  # Calls the make_sound method of Dog class (Woof)
animal_sounds(animal2)  # Calls the make_sound method of Cat class (Meow)
