class Shop:
    cart = []   # class attribute

    def __init__(self, buyer):
        self.buyer = buyer
    
    def add_to_cart(self, item):
        self.cart.append(item)

mehu = Shop(buyer="Mehzabeen")
mehu.add_to_cart("Shoes")
mehu.add_to_cart("Phone")
print(mehu.cart)    # output: ['Shoes', 'Phone']

nisho = Shop(buyer="Nisho")
nisho.add_to_cart("Cap")
nisho.add_to_cart("Watch")
print(nisho.cart)   # output: ['Shoes', 'Phone', 'Cap', 'Watch']

# but nisho'r item alada print dicche na,
# alada print deyar jonno, we will use instance attribute.