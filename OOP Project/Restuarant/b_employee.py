# a -> create customer class
from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address, money):
        super().__init__(name, phone, email, address)
        self.wallet = money
        self.__order = None

    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self, order):
        self.__order = order

    def place_order(self, order):
        self.order = order
        print(f"{self.name} placed an order {order.items}.")
    
    def eat_food(self, order):
        print(f"{self.name} item food {order.items}.")

    def pay_for_order(self, amount):
        pass
    def give_tips(self, tips_amount):
        pass
    def write_review(self, stars):
        pass


# b -> different types of employee (server, chef)
class Employee(User):
    def __init__(self, name, phone, email, address, salary, dept):
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.dept = dept

class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, dept, cooking_item):
        super().__init__(name, phone, email, address, salary, dept)
        self.cooking_item = cooking_item

class Server(Employee):
    def __init__(self, name, phone, email, address, salary, dept):
        super().__init__(name, phone, email, address, salary, dept)
        self.tips_earning = 0
    
    def take_order(self, order):
        pass

    def transfer_order(self, order):
        pass

    def serve_food(self, order):
        pass

    def receive_tips(self, amount):
        self.tips_earning += amount
