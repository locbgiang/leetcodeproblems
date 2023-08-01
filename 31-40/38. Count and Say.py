'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. 
Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":
two 3's, three 2's, one 5, and one 1
2 3 + 3 2 + 1 5 + 1 1
"23321511"
Given a positive integer n, return the nth term of the count-and-say sequence.

Example 1:
Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
'''
def countAndSay(n):
    if n == 1:                  # base case
        return '1'
    else:
        prevS = countAndSay(n-1)        # return the previous string and save to prevS
        current = prevS[0]              # pointer current to first letter
        count = 0                       # count how many letters
        answer = ''
        for i in prevS:                 # iterate through the previous string
            if current == i:            # if the current i letter is the same as the "current" pointer
                count += 1              # increase count by 1
            elif current != i:          # if i is not the same as 'current' pointer
                answer += str(count)    # add count as string to answer
                answer += current       # add current to answer
                current = i             # set current as i
                count = 1               # set count to 1 
        answer += str(count)        # after the for loop add count and current to answer too
        answer += current
        return answer               # return the answer string


n = 5
print(countAndSay(n))