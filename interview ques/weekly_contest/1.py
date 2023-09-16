"""
8029. Points That Intersect With Cars
You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line. For any index i,
nums[i] = [starti, endi] where starti is the starting point of the ith car and endi is the ending point of the ith car.

Return the number of integer points on the line that are covered with any part of a car.
"""


def numberOfPoints(nums):
    obj = set()
    for i in range(len(nums)):
        start = nums[i][0]
        end = nums[i][1]
        for j in range(start, end+1):
            obj.add(j)
    return len(obj)


nums = [[1, 3], [5, 8]]
# nums = [[3, 6], [1, 5], [4, 7]]
print(numberOfPoints(nums))