def count_xyz(K, S):
    count = 0
    for x in range(K+1):
        for y in range(K+1):
            for z in range(K+1):
                if x + y + z == S:
                    count += 1
    return count

# Input K and S
K, S = map(int, input().split())

# Call the function and print the result
print(count_xyz(K, S))
