'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''
def maxSubArray(nums):
    sub = nums[0]       # set sub at first index
    maxSub = sub        

    for i in range(1, len(nums)):
        sub = max(sub+nums[i], nums[i]) # save sub as either sub + nums[i] or nums[i]
        # do this because we can ignore everything that comes before nums[i] if nums[i] is greater than their sum
        if maxSub < sub:
            maxSub = sub        # set new maxSub if sub is greater than current maxSub
    return maxSub

nums = [1]
maxSubArray(nums)