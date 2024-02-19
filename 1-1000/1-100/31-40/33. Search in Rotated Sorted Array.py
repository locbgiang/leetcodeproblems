'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
'''
def search(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left+right)//2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:         # check if left half is sorted
            if nums[left] <= target <= nums[mid]:   # if left half is sorted AND target in in left half 
                right = mid - 1                     # move right pointer to mid
            else:                           # if left half is sorted BUT target not in left half
                left = mid + 1              # move left pointer to mid
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# [5,6,7,0,1,2,3,4]
nums = [5,6,7,0,1,2,3,4]
target = 6
print(search(nums, target))