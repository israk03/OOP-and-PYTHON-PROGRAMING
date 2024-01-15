global_variable = "I am global"

def example_function():
    local_variable = "I am local"
    global global_variable
    global_variable = "Modified global"

    print(local_variable)      # Accessing local variable
    print(global_variable)     # Accessing global variable

example_function()

# print(local_variable)        # This would result in an error (local_variable is not defined in this scope)
print(global_variable)         # Accessing global variable outside the function
