'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''


def groupAnagrams(strs):
    mem = {}
    for str in strs:
        arr = list(str)                 # turn str into list
        arr.sort()                      # sort list
        if "".join(arr) not in mem:         # check if the string of list is in memory
            mem["".join(arr)] = [str]       # if it is not in memory, save to memory
        else:
            mem["".join(arr)] += [str]      # otherwise add the string to the string already existing in memory
    return [i for i in mem.values()]        # loop through memory and return all the values
    


strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)