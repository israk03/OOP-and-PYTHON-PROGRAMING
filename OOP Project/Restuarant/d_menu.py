# d -> menu class with pizza, burger, drinks
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cooking_time = 15

class Burger(Food):
    def __init__(self, name, price, meat, ingredients):
        super().__init__(name, price)
        self.meat = meat 
        self.ingredients = ingredients

class Pizza(Food):
    def __init__(self, name, price, size, toppings):
        super().__init__(name, price, size)
        self.size = size
        self.toppings = toppings

class Drinks(Food):
    def __init__(self, name, price, isCold = True):
        super().__init__(name, price)
        self.isCold = isCold

class Menu:
    def __init__(self):
        self.pizzas = []
        self.burgers = []
        self.drinkss = []

    def add_menu_item(self, item_type, item):
        if item_type == 'pizza':
            self.pizzas.append(item)
        elif item_type == 'burger':
            self.burgers.append(item)
        elif item_type == 'drinks':
            self.drinkss.append(item)

    def show_menu(self):
        for pizza in self.pizzas:
            print(f"Name: {pizza.name} Price: {pizza.price}.")
        for burger in self.burgers: 
            print(f"Name: {burger.name} Price: {burger.price}.")
        for drinks in self.drinkss:
            print(f"Name: {drinks.name} Price: {drinks.price}.")