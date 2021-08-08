'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

def threeSumClosest(nums, target):
    '''if len(nums) < 3:
        return []
    nums.sort()
    for i in range(1, len(nums)-1):
        left = 0
        right = len(nums)-1
        total = 0
        distance = 0
        answer = 0
        while left < i and right > i:
            total = nums[left] + nums[right] + nums[i]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
        
        if total <= 0:
            distance = target - total
        else:
            distance = total - target
            
        if answer == 0:
            answer = total
        if distance < answer:
            answer = total
    return answer
    '''

    '''
    print(nums)
    print(nums[left], nums[mid], nums[right])
    print(total)
    
    nums.sort()
    left = 0
    mid = int((len(nums)-1)/2)
    right = len(nums)-1
    running = True
    while running:
        total = nums[left] + nums[mid] + nums[right]
        if total == target:
            return total
        elif total < target:
            mid += 1
        elif total > target:
            mid -= 1
        print(total)
    '''
    print(nums)
    nums.sort()
nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))