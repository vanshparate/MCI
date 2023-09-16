"""
O(n^2) or O(n*n)
"""

boxes = ['a', 'b', 'c', 'd', 'e']


def log_all_pairs(array):
    for i in array:
        for j in array:
            print(i, j)


log_all_pairs(boxes)
