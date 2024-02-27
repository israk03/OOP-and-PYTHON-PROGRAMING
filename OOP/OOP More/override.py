class Animal:
    def make_sound(self):
        print("Generic animal sound.")

class Dog(Animal):
    # override
    def make_sound(self):
        print("Wooof.")

class Cat(Animal):
    # override
    def make_sound(self):
        print("Meoww.")

animal = Animal()
dog = Dog()
cat = Cat()

animal.make_sound()
dog.make_sound()
cat.make_sound()