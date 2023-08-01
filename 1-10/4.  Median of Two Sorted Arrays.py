'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''
import math
nums1 = [1,3]
nums2 = [2]

# Solution:
def findMedianSortedArrays(nums1,nums2):
    mergedArray = nums1 + nums2
    mergedArray.sort()

    if len(mergedArray)%2 == 0:                         # if merged array is even length, add the two middle numbers and divide by 2
        median = (mergedArray[int(len(mergedArray)/2-1)] + mergedArray[int(len(mergedArray)/2)])/2
        return median
    else:                                               # if odd length, just return the middle number
        median = (mergedArray[math.floor(len(mergedArray)/2)])
        return median
# Solution
print(findMedianSortedArrays(nums1, nums2))