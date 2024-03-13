import math
import time
def timer(func):
    def inner(*args, **kwargs):
        print("Time started")
        start = time.time()
        func(*args, **kwargs)
        print("Time ended")
        end = time.time()
        print(f"Total time taken {end-start}.")
    return inner

@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f"Factorial of {n} is: {result}")

get_factorial(5)