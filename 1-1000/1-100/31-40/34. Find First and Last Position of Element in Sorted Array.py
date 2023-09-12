'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]


Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
'''

def searchRange(nums, target):
    def search(target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    left = search(target)               # search left most value of target
    right = search(target+1) - 1        # search the left most value of target+1, then - 1
    
    if left <= right:
        return [left, right]
    return [-1, -1]


nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target))