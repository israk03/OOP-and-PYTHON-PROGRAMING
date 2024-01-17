try:
    num = int(input("Enter a number:"))
    res = 10 / num
    print("Result: ", res)

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cant divided by 0.")

finally:
    print("Finally block: This will always be executed.")