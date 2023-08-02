'''
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"

Example 3:
Input: n = 3, k = 1
Output: "123"
'''

'''
example:
n = 4,  k = 9

1234    2134    3124    4123
1243    2143    3142    4132
1324    2314    3214    4213
1342    2341    3241    4231
1423    2413    3412    4312
1432    2431    3421    4321

note that there are 24 choices total.  first number changes every n!//len(nums) = 4!//4 = 24//4 = 6 = (n-1)!
given k = 9-1 = 8 since our index starts at 0 and not 1
we can find that the first number is 2
k//(n-1)! = 8//6 = 1
remainder = 2 = k
since nums = [1, 2, 3, 4]
nums[1] = 2


after the first number (2), we are left with these choices
134     314     413
143     341     431

note that the next number changes every (n-1)!//len(nums) = (n-2)! = 2 spots
k//(n-2)! = 2//2 = 1
remainder = 0 = k
since nums = [1, 3, 4]
nums[1] = 3

we are left with
14      41
now (n-3)! = (4-3)! = (1)! = 1
k//(n-3)! = 0//1 = 0
k = k%0 = 0
nums = [1, 4]
nums[0] = 1

we are left with
4
k//(n-3)! = 0//1 = 0
nums[0] = 4

answer = 2314
'''
from math import factorial
def getPermutation(n, k):
    nums = [str(i) for i in range(1, n+1)]
    fact = factorial(n)
    answer = []
    k = k-1

    while nums:
        fact = fact // len(nums)
        index = k//fact
        k = k%fact
        answer.append(nums.pop(index))
    return "".join(answer)

n = 4
k = 9
getPermutation(n, k)