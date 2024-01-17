# Example of dictionaries

# Creating a dictionary
person = {"name": "Alice", "age": 25, "city": "Wonderland"}

# Accessing elements
print("Name:", person["name"])
print("Age:", person["age"])

# Modifying values
person["age"] = 26
print("Modified Age:", person["age"])

# Adding a new key-value pair
person["gender"] = "Female"
print("Updated Dictionary:", person)

# Removing a key-value pair
del person["city"]
print("Dictionary after removing 'city':", person)

# Dictionary methods
keys = person.keys()
values = person.values()
items = person.items()

print("Keys:", keys)
print("Values:", values)
print("Items:", items)

# Using get() method
city_value = person.get("city", "City Not Found")
print("City (using get()):", city_value)

# Using pop() method
gender_value = person.pop("gender", "Gender Not Found")
print("Popped Gender:", gender_value)

# Using update() method
person.update({"city": "New Wonderland", "country": "Fantasia"})
print("Updated Dictionary:", person)

# Nested dictionaries
nested_dict = {
    "person": {"name": "Charlie", "age": 35},
    "location": {"city": "Cloudville", "country": "Skyland"}
}
print("Nested Dictionary:", nested_dict)

# Iterating through a dictionary
print("Iterating through keys:")
for key in person:
    print(f"Key: {key}, Value: {person[key]}")

print("\\nIterating through items:")
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")
