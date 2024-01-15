# Creating a list
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "apple", 3.14, True]

# Accessing elements of a list
print(fruits[0])  # Output: apple
print(numbers[-1])  # Output: 5 (negative index counts from the end)

# Methods
# Adding an element to the end of the list
fruits.append("orange")
print(fruits)

# Inserting an element at a specific position
fruits.insert(1, "grape")
print(fruits)

# Removing a specific element
fruits.remove("banana")
print(fruits)

# Removing and returning the last element
removed_item = fruits.pop()
print(removed_item)
print(fruits)

# Finding the index of an element
index_of_cherry = fruits.index("cherry")
print(f"Index of 'cherry': {index_of_cherry}")

# Counting occurrences of an element
count_of_apple = fruits.count("apple")
print(f"Count of 'apple': {count_of_apple}")

# Sorting the list in-place
fruits.sort()
print(fruits)

# Reversing the order of the list in-place
fruits.reverse()
print(fruits)
