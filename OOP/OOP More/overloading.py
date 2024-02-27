class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Addition overloading
    def __add__(self, other):
        combined_title = f"{self.title} and {other.title}"
        combined_author = f"{self.author} and {other.author}"  # Fixed this line
        return Book(combined_title, combined_author)

    # Subtraction overloading
    def __sub__(self, other):
        if self.title == other.title and self.author == other.author:
            return None
        else:
            return Book(f"Difference of {self.title} and {other.title}", f"{self.author} and {other.author}")

    # Multiplication overloading
    def __mul__(self, quantity):
        multiplied_title = f"{quantity} copies of {self.title}"
        multiplied_author = f"{quantity}x {self.author}"  # Fixed the variable name
        return Book(multiplied_title, multiplied_author)

# Usage
book1 = Book("Harry Potter", "J.K.R.")
book2 = Book("Game of Thrones", "G.R.R.M.")

# Addition
combined_book = book1 + book2
print(f"Combined book: {combined_book}")

# Subtraction
difference_book = book1 - book2  # Assigned the result to difference_book
print(f"Difference book: {difference_book}")

# Multiplication
multi_book = book1 * 3
print(f"Multiplied book: {multi_book}")
