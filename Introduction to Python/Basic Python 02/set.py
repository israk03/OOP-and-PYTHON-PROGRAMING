set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
print(f"The first set: {set1}")

# adding elements
set1.add(6)
set1.update({7,8,9})

# removing elements
set1.remove(3)
set1.discard({7,8,9})

print("Set 1: ", set1)
print("Set 2: ", set2)

#operations
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
symmetric_set = set1.symmetric_difference(set2)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
print("Symmetric Difference:", symmetric_set)