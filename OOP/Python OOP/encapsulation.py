class Example:
    def __init__(self):
        self.public = "I am public."
        self._protected = "I am protected."
        self.__private = "I am private."

    def display_info(self):
        print("Accessing members:")
        print(f"Public member: {self.public}")
        print(f"Protected member: {self._protected}")
        print(f"Private member: {self.__private}")

obj = Example()

print(f"Accessing public member from outside the class: {obj.public}")

print(f"Accessing protected member from outside the class: {obj._protected}")

# print(f"Accessing private member from outside the class: {obj.__private})
# this will give error
print(f"Accessing private member from outside the class by trick: {obj._Example__private}")


