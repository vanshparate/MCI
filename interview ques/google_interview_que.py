# [1, 2, 3, 9]
# [1, 2, 4, 4]
# Target Sum = 8. Linked Lists

# array1 = [1, 2, 3, 9]
array1 = [1, 2, 4, 4]
target = 8

# Brute Force
# Time complexity - O(n^2)  [Quadratic]
"""
def sum_equals_target(arr1):
    for i in range(len(arr1)):
        for j in range(i+1, len(arr1)):
            if arr1[i] + arr1[j] == target:
                return True
    return False


print(sum_equals_target(array1))
"""


# Time complexity - O(n)  [Linear]
"""
def sum_equals_target2(arr1):
    low = 0
    high = len(arr1) - 1
    while low < high:
        s = arr1[low] + arr1[high]
        low += 1
        if s == target:
            return True


print(sum_equals_target2(array1))
"""


# Hash Set
def sum_equals_target3(arr1):
    comp = set()
    for value in arr1:
        if value in comp:
            return True
        comp.add(target - value)
    return False


print(sum_equals_target3(array1))
