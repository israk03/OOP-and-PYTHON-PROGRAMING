def function_name(n1, n2, *args, **kargs):
    print(f"n1: {n1}")
    print(f"n2: {n2}")
    print(f"Additional positional arguments: {args}")
    print(f"Additional keyword arguments: {kargs}")

# Calling the function with different arguments
function_name(1, 2, 3, 4, 5, name="Alice", age=25)
