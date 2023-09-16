# Given two arrays, create a function that let's user know (True/False) whether these two arrays contain any common items

ar1 = ['a', 'b', 'c', 'x']
ar2 = ['z', 'y', 'f']


# def common(arr1, arr2):
#     for i in range(len(arr1)):
#         for j in range(len(arr2)):
#             if arr1[i] == arr2[j]:
#                 return True
#     return False
#
#
# print(common(ar1, ar2))


def common2(arr1, arr2):
    obj = {}
    for i in range(len(arr1)):
        if arr1[i] not in obj:
            obj[arr1[i]] = True

    for j in range(len(arr2)):
        if arr2[j] in obj:
            return True
    return False


print(common2(ar1, ar2))