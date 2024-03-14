# Sum of Consecutive Odd Numbers
def sum_of_odds(x, y):
    total = 0
    for num in range(x+1, y):
        if num % 2 != 0:
            total += num
    return total

print("Please enter the number of test cases: ")
t = int(input())

for _ in range(t):
    x, y  = map(int, input().split())

    print(sum_of_odds(x, y))