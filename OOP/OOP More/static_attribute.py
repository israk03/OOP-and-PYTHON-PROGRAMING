class my_class:
    static_variable = 10 # static attribute

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

print(my_class.static_variable) # accessing the static attribute using the class name

