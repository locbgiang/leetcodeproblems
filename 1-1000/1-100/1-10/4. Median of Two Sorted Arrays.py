'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''
import math
nums1 = [1,3]
nums2 = [2,4]

# Solution:
def findMedianSortedArrays(nums1,nums2):
    new = nums1 + nums2
    new.sort()
    mid = (len(new)-1)/2
    if len(new)%2 == 1 or len(new) <= 1:
        answer = new[int(mid)]
    else:
        answer = (new[int(mid)] + new[int(mid+1)]) / 2.0

    return answer
# Solution
print(findMedianSortedArrays(nums1, nums2))