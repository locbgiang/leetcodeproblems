'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2
'''

def searchInsert(nums, target):             # binary search to get O(log(n))
    left = 0                                # left pointer
    right = len(nums) - 1                   # right pointer
    while left <= right:                    # run loop while left <= than right
        mid = (left+right)//2               # find mid
        if (target == nums[mid]):           # if target = mid then return mid
            return mid                      
        elif (target > nums[mid]):          # else if target > mid
            left = mid + 1                  # move left to mid + 1
        else:
            right = mid - 1                 # move right to mid - 1
    return left                         # if there is no target, return left

nums = [1,3,5,6]
target = 5

print(searchInsert(nums, target))