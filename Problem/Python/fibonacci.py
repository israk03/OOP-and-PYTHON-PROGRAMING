# Easy Fibonacci
def fibonacci(n):
    fibo_num = [0, 1]
    for i in range(2, n):
        next = fibo_num[-1] + fibo_num[-2]
        fibo_num.append(next)
    return fibo_num[:n]

n = int(input("Enter the value: "))

print("First", n, "numbers of fibonacci series:")
print(fibonacci(n))