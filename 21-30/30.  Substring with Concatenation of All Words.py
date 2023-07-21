'''
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. 
"acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.
 
Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
There is no substring of length 16 is s that is equal to the concatenation of any permutation of words.
We return an empty array.
'''

def findSubstring(s, words):
    lenWord = len(words[0])
    lenAllWords = lenWord * len(words)
    wordsCounter = {}
    answer = []

    for word in words:
        if word in wordsCounter:
            wordsCounter[word] += 1
        else:
            wordsCounter[word] = 1
    
    for i in range(len(s)-lenAllWords+1):
        cutS = s[i:i+lenAllWords]
        cutSCounter = {}
        
        for j in range(0, lenAllWords, lenWord):
            cutword = cutS[j:j+lenWord]
            if cutword in cutSCounter:
                cutSCounter[cutword] += 1
            else:
                cutSCounter[cutword] = 1
        if wordsCounter == cutSCounter:
            answer.append(i)
    print(answer)       
    return


s = 'barfoothefoobarman'
words = ["foo","bar"]
findSubstring(s, words)