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
n = 4,  k = 9, nums = [1,2,3,4]

1234    2134    3124    4123
1243    2143    3142    4132
1324    2314    3214    4213
1342    2341    3241    4231
1423    2413    3412    4312
1432    2431    3421    4321

see that there are 24 unique permutations total.
n! = 4! = 24
first number repeats 6 times before changing, lets call it row.
there are 4 different choices for the first number, lets call the number of choices column.
row * column = n!
row = n! / column (choices)
row = 24 / 4 = 6. math checks out.

now for k = 9 means that we will run this permutation 9 times
we know that the first number cannot be 1 since 9 > 6
just from looking, we can tell that it will end up at 2 but lets do the math
let k = k - 1 since we will use k to calculate our index
index = k//row = 8//6 = 1
remainder = 2 = k
nums = [1, 2, 3, 4] this is our column
nums[1] = 2

after the first number, we are left with these (2nd column above but remove 2)
134
143
314
341
413
431
we can arrange it like this for clarity
134     314     413
143     341     431
there are now 6 possibilities left. (same as row from above)
(n-1)! = 3! = 6
the first number repeats 2 times before changing. 
3 different choices.
math:  row = (n-1)!/column = 6/3 = 2
k = 2, the remainder 
index = k//row = 2//2 = 1
remainder = 0 = k
nums = [1, 3, 4]
nums[1] = 3

we are left with
14      41
k//row = 0//1 = 0
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
    nums = [str(i) for i in range(1, n+1)]  # an array of possible numbers
    fact = factorial(n)     # n! 
    answer = []
    # since we will use k for the calculation of our index, and array index starts at 0 we must subtract 1 from k
    k = k-1                 

    while nums:
        fact = fact // len(nums)        # how many times the choice repeats before changing
        index = k//fact                 # the index of nums
        k = k%fact                      # the remainder
        answer.append(nums.pop(index))  # append the value at index from nums into answer 
    return "".join(answer)

n = 4
k = 9
getPermutation(n, k)