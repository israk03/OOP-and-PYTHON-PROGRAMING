def all_sum(*num):
    print(num)
    sum = 0
    for n in num:
        print(n)
        sum += n
    return sum

total = all_sum(3,4,5,8)
print(total)