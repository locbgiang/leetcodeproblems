'''
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''

def searchMatrix(matrix, target):
    length = len(matrix[0])
    left = 0
    right = (len(matrix) * length) - 1 
    
    while left <= right:
        mid = (left + right) // 2
        row = mid // length
        col = (mid % length)
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False
matrix = [[1]] 
target = 1
print(searchMatrix(matrix, target))