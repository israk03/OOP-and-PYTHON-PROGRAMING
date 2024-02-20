from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def info(self):
        pass

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def info(self):
        print(f"{self.name} - circle with radius {self.radius}.")

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width 
    def area(self):
        return self.length * self.width
    def info(self):
        print(f"{self.name} - rectangle with length {self.length} and width {self.width}")

circle1 = Circle("circle1", 5)
rectangle1 = Rectangle("RECT1", 8, 4)

print(circle1.area())
circle1.info()

print(rectangle1.area())
rectangle1.info()
        