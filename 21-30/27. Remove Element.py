'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

def removeElement(nums, val):
    L = 0                               # Left pointer starts at 0
    for R in range(0, len(nums)):           
        if nums[R] != val:              # If right pointer number != val
            nums[L] = nums[R]           # set left pointer to the right number 
            L += 1                      # move left pointer up
    return L
nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))