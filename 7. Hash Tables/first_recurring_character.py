# Google Question
# Given an array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# It should return 2

# Given an array = [2, 1, 1, 2, 3, 5, 1, 2, 4]
# It should return 1

# Given an array = [2, 3, 4, 5]
# It should return undefined


"""
# Using arrays
# Time complexity O(n^2)
# Space Complexity O(1)

def recurring(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                return array[i]
    return "undefined"


# array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
array = [2, 3, 4, 5]
print(recurring(array))
"""



# Using hash tables
# Time Complexity O(n)
# Space Complexity O(n)
def recurring2(array):
    items = {}
    for item in array:
        if item in items:
            return item
        else:
            items[item] = True
    return None


array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# array = [2, 3, 4, 5]
print(recurring2(array))