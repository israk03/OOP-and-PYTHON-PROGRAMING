class Shop:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, item, quantity, price):
       product = {'item': item, 'quantity': quantity, 'price': price}
       self.cart.append(product)

    def chekout(self, amount):
        total = 0
        for item in self.cart:
            #print(item)
            total += item['price'] * item['quantity']

        print(f"Total price: {total}tk.")

        if amount < total:
            print(f"Please provide {total-amount}tk more.")
        else:
            print(f"Here is your extra {amount-total}tk. Thak you.")

mic = Shop()
mic.add_to_cart("alu", 5, 50)
mic.add_to_cart("chal", 10, 90)
print(mic.cart)
mic.chekout(10000)