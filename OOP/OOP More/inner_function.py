def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Usage
closure = outer_function(10)
result = closure(5)  # Calls the inner function with y=5
print(result)  # Output: 15
