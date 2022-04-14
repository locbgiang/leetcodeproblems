'''
Given an array nums of n integers, return an array of all the unique quadruplets 
[nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
'''

'''
def foursum (nums, target):
    nums.sort()
    answer = []
    inArr = []
    for i in range(0, len(nums)-3):
        for j in range(i+1, len(nums)-2):
            for k in range(j+1, len(nums)-1):
                for l in range(k+1, len(nums)):
                    if target == nums[i]+nums[j]+nums[k]+nums[l]:
                        inArr.append(nums[i])
                        inArr.append(nums[j])
                        inArr.append(nums[k])
                        inArr.append(nums[l])
                        if inArr not in answer:
                            answer.append(inArr)
                        inArr = []
    return answer
'''    

def foursum (nums, target):
    nums.sort()
    answer = []
    inArr = []
    for i in range(0, len(nums)-3):                 # fartest left
        for j in range(i+1, len(nums)-2):           # 2nd fartest left
            start = j+1                             # pointer start for while loop
            end = len(nums)-1                       # pointer end 
            while start < end:
                sum = nums[i]+nums[j]+nums[start]+nums[end]
                if sum < target:                    # if sum less than target move pointer up
                    start += 1
                elif sum > target:                  # if sum greater than target move end pointer down
                    end -= 1    
                elif sum == target:                 # if found sum append the number
                    inArr.append(nums[i])
                    inArr.append(nums[j])
                    inArr.append(nums[start])
                    inArr.append(nums[end])
                    if inArr not in answer:
                        answer.append(inArr)
                    inArr = []
                    start += 1                      # move start pointer up 
    return answer
nums=[-3,-2,-1,0,0,1,2,3]
#nums = [1,0,-1,0,-2,2] 
#nums = [2,2,2,2,2]
target = 0
foursum(nums, target)
print(nums)