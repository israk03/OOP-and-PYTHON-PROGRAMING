# variable_name = input("-----------")

money = input("Give me some money: ")
print("Here is your money:",money)

first_money = input("Kodom Ali give me some money: ")
second_money = input("Peyara Bhanu give me some money: ")

"""
total = first_money + second_money
print("I got : ", total)

WRONG!!! Cz by default the input from
user will be string type.
"""

first_money_int = int(first_money)
second_money_int = int(second_money)

total = first_money_int + second_money_int
print("I got total", total, "tk.")




