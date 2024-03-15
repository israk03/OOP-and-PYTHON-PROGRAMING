# create a product class and a shop class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []

    def list_products(self):
        if not self.products:
            print("No product available.")
        else:
            print("Products available in", self.name + ":")
            for p in self.products:
                print("-", p.name, "(TK.", p.price, ")")

p1 = Product("Laptop", 52000)
p2 = Product("iPhone", 36000)

my_shop = Shop("My Shop")

my_shop.products.append(p1)
my_shop.products.append(p2)

my_shop.list_products()