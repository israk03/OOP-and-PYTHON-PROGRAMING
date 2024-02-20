# common base class
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print (f"{self.name} says {self.sound}!")

#inherited class (common)
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meowwww")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Wooouuuuuf")

# inherited class (uncommon)
class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, "Tweeet")

    def fly(self):
        print(f"{self.name} is flying.")


cat = Cat("Micky")
dog = Dog("Bob")
bird = Bird("Poi")

cat.make_sound()
dog.make_sound()
bird.fly()

