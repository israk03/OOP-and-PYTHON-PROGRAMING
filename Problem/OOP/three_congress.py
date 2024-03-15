# Inside the Shop class, create a method name buy_product which is used to buy a product and check whether this product is available or not. If you successfully buy a product, then throw a Congress message.

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
            print("No products available.")
        else:
            print("Products available in", self.name + ":")
            for product in self.products:
                print("-", product.name, "($", product.price, ")")


    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added to {self.name}.")

    def buy_product(self, product_name):
        for product in self.products:
            if product_name == product_name:
                print(f"Congratulations! You bought {product.name} from {self.name}.")
                self.products.remove(product)
                return 
        print(f"Sorry, {product_name} is not available in {self.name}.")

p1 = Product("Laptop", 52000)
p2 = Product("iPhone", 36000)

my_shop = Shop("My Shop")

my_shop.buy_product("Laptop")
my_shop.buy_product("iPhone")

my_shop.list_products()