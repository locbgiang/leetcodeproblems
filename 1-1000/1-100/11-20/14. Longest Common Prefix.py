'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
'''

# Solution:
def longestCommonPrefix(strs):
    prefix = ''
    if len(strs) == 0:                     # check outter case if there are no word, return empty string
        return prefix
    elif len(strs) == 1:                    # if there is one word, return the word
        return strs[0]
    else:                                # if there are more than 1 word, return the length of the first word
        length = len(strs[0])
    counter = 0
    while counter < length:           # while loop the entire first word
        for i in range(1, len(strs)):           # for loop to compare each letter of the first word with coresponding letter of every other word
            if len(strs[i]) > counter:          # if the current word has more letters than the current letter
                if strs[0][counter] != strs[i][counter]:       # compare the letter of the first word to the letter of the other word
                    return prefix                  # return the prefix if they do not match
            else:
                return prefix                # return the prefix if the word is shorter than the current letter position
        prefix += strs[0][counter]         # add the letter to the prefix if every word contains the letter
        counter += 1                    # go to the next letter
    return prefix


    

# Solution

#strs = ["flower","flow","flight"]
strs = ['ab', 'a']
print(longestCommonPrefix(strs))