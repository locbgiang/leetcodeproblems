'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
'''


def climbStairs(n):
        one, two = 1, 1
        for i in range(n-1):
            temp = one+two
            one = two
            two = temp
            print('two is ', two)
        return two

n = 2
print(climbStairs(5))
