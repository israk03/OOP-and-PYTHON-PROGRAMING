class Dog:
    species = 'Canine'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name} says wooooof!')

dog1 = Dog(name="Max", age=3)
dog2 = Dog(name="Bob", age=5)

print(f"{dog1.name} is {dog1.age} years old.")
print(f"{dog2.name} is {dog2.age} years old.")

dog1.bark()
dog2.bark()