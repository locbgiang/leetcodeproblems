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
    # typical binary search except we need to pay attention to the left and right tree since they have pivot
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[left]:                       # this means nums[mid] is on the left tree
            if target > nums[mid] or target < nums[left]:   
                # (target > nums[mid]) means there are more of the left tree, move left pointer to mid
                # (target < nums[left]) means the target is on the right tree, since mid is on the left tree the entire right tree is to the right
                left = mid + 1
            else:
                # otherwise, (target < nums[mid]) must be true, move right pointer to mid
                right = mid - 1
        else:                       # (nums[mid] < nums[right]) must be true, we are on the right tree
            if target < nums[mid] or target > nums[right]:
                # (target < nums[mid]) means that there are smaller number on the right tree
                # (target > nums[right]) means the left tree contains more number
                right = mid - 1
            else:
                # (target < nums[left]) otherwise must be true, target is on the right tree
                left = mid + 1
    return -1
            

nums = [4,5,0,1,2,3] 
target = 0
print(search(nums, target))