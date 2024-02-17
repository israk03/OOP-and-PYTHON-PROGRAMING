class Circle:
    pi = 3.1416

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * self.radius ** 2
    
    def circum(self):
        return self.pi * self.radius * 2
    
my_circle = Circle(radius=5)

area_result = my_circle.area()
circum_result = my_circle.circum()

print("Area of circle:", area_result)
print("Circumference of the circle:", circum_result)