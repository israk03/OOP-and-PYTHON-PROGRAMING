fruits = ("apple", "banana", "grape", "orange")
print(f"The fruits are: {fruits}")

print("First fruit: ", fruits[0])
print("Last fruit: ", fruits[-1])

# unpacking
first_fruit, sec_fruit, *rest_fruits = fruits
print("First fruit: ", first_fruit)
print("Second fruit: ", sec_fruit)
print("Rest of fruits: ", rest_fruits)

# some methods
count_of_apple = fruits.count("apple")
index_of_grape = fruits.index("grape")

print("Count of apple: ", count_of_apple)
print("Index of grape: ", index_of_grape)

# Returning multiple values from a function using a tuple
def get_rectangle_dimensions(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

rectangle_area, rectangle_perimeter = get_rectangle_dimensions(5, 8)
print("Rectangle Area:", rectangle_area)
print("Rectangle Perimeter:", rectangle_perimeter)