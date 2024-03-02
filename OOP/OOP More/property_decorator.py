class myclass:
    def __init__(self, value):
        self._value = value

    # getter method
    @property
    def value(self):
        return self._value
    
    # setter method
    @value.setter
    def value(self, new_value):
        if new_value >= 0:
            self._value = new_value
        else:
            print("Value must be non-negative.")

    # read only property
    @property
    def square(self):
        return self._value ** 2
    
obj = myclass(5)

print(obj.value)

obj.value = 8
print(obj.value)

obj.value = -3
print(obj.value)

print(obj.square)