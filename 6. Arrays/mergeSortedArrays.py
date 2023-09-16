ar1 = [0, 3, 4, 31]
ar2 = [4, 6, 30]

# ar1 = [1,3,5,7]
# ar2 = [2,4,6,8. Linked Lists,10,12]


def mergeSortedArrays(array1, array2):
    new_array = []
    flag = 0
    index_of_first_array = index_of_second_array = 0
    while not (index_of_first_array >= len(array1) or index_of_second_array >= len(array2)):
        if array1[index_of_first_array] <= array2[index_of_second_array]:
            new_array.append(array1[index_of_first_array])
            index_of_first_array += 1
        else:
            new_array.append(array2[index_of_second_array])
            index_of_second_array += 1

        if index_of_first_array == len(array1):
            flag = 1

    if flag == 1:
        for item in array2[index_of_second_array:]:
            new_array.append(item)
    else:
        for item in array1[index_of_first_array:]:
            new_array.append(item)
        for item in array2[index_of_second_array:]:
            new_array.append(item)

    return new_array


print(mergeSortedArrays(ar1, ar2))
