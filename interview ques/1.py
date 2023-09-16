"""
Given 2 arrays, create a function that let's user know (true/false) whether these two arrays contain any common items.
For Example:
array_1 = ['a', 'b', 'c', 'x']
array_2 = ['z', 'y', 'i']
should return false
-------------------
array_1 = ['a', 'b', 'c', 'x']
array_2 = ['z', 'y', 'x']
should return true
"""


array_1 = ['a', 'b', 'c', 'x']
array_2 = ['z', 'y', 'x']


# def contains_common_item(arr1, arr2):
#     for i in arr1:
#         for j in arr2:
#             if i == j:
#                 return True
#     return False

def contains_common_item(arr1, arr2):
    for i in arr1:
        if i in arr2:
            return True
    return False


print(contains_common_item(array_1, array_2))