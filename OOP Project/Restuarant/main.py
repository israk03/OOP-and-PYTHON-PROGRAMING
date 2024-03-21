from d_menu import Pizza, Burger, Drinks, Menu
from c_restuarant import Restuarant
from b_employee import Chef, Customer, Server, Manager
from e_order import Order

def main():
    menu = Menu()

    pizza_1 = Pizza('Chicken Pizza', 600, 'Large', ['Chicken', 'Onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('Beef Pizza', 800, 'Medium', ['Beef', 'Onion'])
    menu.add_menu_item('pizza', pizza_2)
    
    burger_1 = Burger('Naga Burger', 300, 'Chicken', ['Chicken', 'Naga'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('Cheess Burger', 300, 'Extra Cheess', ['Cheesss'])
    menu.add_menu_item('burger', burger_2)

    coke = Drinks('Cocacola', 50, True)
    menu.add_menu_item('drinks', coke)
    mocha = Drinks('Mocha Coffee', 300, False)
    menu.add_menu_item('drinks', mocha)

    menu.show_menu()


    restuarant = Restuarant('Sai Baba Restuarant')

    manager = Manager('Kala Chan', 8888, 'kala@chan.com', 'kalipur', 1500, 'core')
    restuarant.add_employee('manager', manager)

    chef = Chef('Rustom', 9999, 'rustom@kopa.com', 'Rustom Nagar', 2500, 'chef')
    restuarant.add_employee('chef', chef)

    server = Server('Chotu', 7777, 'nai@jai.com', 'Restuarant', 1000, 'server')
    restuarant.add_employee('server', server)

    restuarant.show_employees()

    customer_1 = Customer('Shakib', 1111, 'sakib@khan.com', 'banani', 100000)
    order_1 = Order(customer_1, [pizza_1, mocha])
    customer_1.pay_for_order(order_1)
    restuarant.add_order(order_1)

    restuarant.receive_payment(order_1, 2000, customer_1)

    print(f"Revenue: {restuarant.revenue}, Balance: {restuarant.balance}.")