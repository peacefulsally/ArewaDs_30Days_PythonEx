#Sets Exercises: Level 2

# Given sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#To Join A and B
A_union_B = A.union(B)
print(f"Union of A and B: {A_union_B}")

#Find A intersection B
A_intersection_B = A.intersection(B)
print(f"Intersection of A and B: {A_intersection_B}")

#Is A a subset of B
is_A_subset_of_B = A.issubset(B)
print(f"Is A a subset of B? {is_A_subset_of_B}")

# Are A and B disjoint sets
are_A_and_B_disjoint = A.isdisjoint(B)
print(f"Are A and B disjoint sets? {are_A_and_B_disjoint}")

# Join A with B and B with A (this is essentially the same as union)
A_with_B = A.union(B)
B_with_A = B.union(A)
print(f"Join A with B: {A_with_B}")
print(f"Join B with A: {B_with_A}")

# What is the symmetric difference between A and B
A_symmetric_difference_B = A.symmetric_difference(B)
print(f"Symmetric difference between A and B: {A_symmetric_difference_B}")

# Delete the sets completely
del A
del B
try:
    print(A)  # Will raise an error because A is deleted
except NameError as e:
    print(f"Error: {e}")

#Level 3 of set Exercise

# Given ages list
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages)
# Convert the ages list to a set
ages_set = set(ages)
print(ages_set)

# Compare lengths of the list and the set
len_list = len(ages)
len_set = len(ages_set)

print(f"Length of ages list: {len_list}")
print(f"Length of ages set: {len_set}")

if len_list > len_set:
    print("The list is bigger.")
else:
    print("The set is bigger (or they are equal).")