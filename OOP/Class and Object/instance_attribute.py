class Shop:

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []  #instance attribute
    
    def add_to_cart(self, item):
        self.cart.append(item)

mehu = Shop(buyer="Mehzabeen")
mehu.add_to_cart("Shoes")
mehu.add_to_cart("Phone")
print(mehu.cart) 

nisho = Shop(buyer="Nisho")
nisho.add_to_cart("Cap")
nisho.add_to_cart("Watch")
print(nisho.cart)