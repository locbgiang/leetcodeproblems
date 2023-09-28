'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique. 
'''
def topKFrequent(nums , k):
    mem = {}
    for i in nums:
        mem[i] = 1 + mem.setdefault(i, 0)
    return [sorted(mem.items(), key = lambda x:-x[1])[i][0] for i in range(0, k)]

nums = [2,3,4,1,4,0,4,-1,-2,-1]
k = 2
p = topKFrequent(nums, k)
print(p)