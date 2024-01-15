# Creating a new list using list comprehension
squares = [x**2 for x in range(5)]
print(squares)
# Output: [0, 1, 4, 9, 16]

# Creating a new list with a condition
even_squares = [x**2 for x in range(5) if x % 2 == 0]
print(even_squares)
# Output: [0, 4, 16]
