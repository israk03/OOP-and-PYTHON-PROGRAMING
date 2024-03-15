# Inside the Shop class, create a method name add_product which adds products using the Product class to the Shop class.


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []

    """def list_products(self):
        if not self.products:
            print("No product available.")
        else:
            print("Products available in", self.name + ":")
            for p in self.products:
                print("-", p.name, "(TK.", p.price, ")")"""

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added to {self.name}.")

p1 = Product("Laptop", 52000)
p2 = Product("iPhone", 36000)

my_shop = Shop("My Shop")

my_shop.add_product(p1)
my_shop.add_product(p2)

#my_shop.list_products()