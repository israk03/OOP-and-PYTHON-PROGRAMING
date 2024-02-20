class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        print(f"{self.brand} -> {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, num_seats):
        super().__init__(brand, model)

        self.num_seats = num_seats
     # Overriding the display_info method from the Vehicle class
    def info(self):
        print(f"{self.brand} {self.model} with {self.num_seats} seats.")

class SportsCar(Car):
    def __init__(self, brand, model, num_seats, speed):
        super().__init__(brand, model, num_seats)

        self.speed = speed
     # Overriding the display_info method from the Car class
    def info(self):
        print(f"{self.brand} {self.model} with speed of {self.speed}mph.")

car = Car("Toyota", "Camry", 4)
sports_car = SportsCar("Ferrari", "458 Italia", 2, 210)

car.info()
sports_car.info()