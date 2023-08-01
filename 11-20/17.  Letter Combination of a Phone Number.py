'''
Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.

2 = abc     3 = def     4 = ghi
5 = jkl     6 = mno     7 = pqrs
8 = tuv     9 = wxyz


Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''

from unittest import result

from black import out


def letterCombination(str):
    if not str:
        return []

    mem = {}
    mem['2'] = ['a', 'b', 'c']
    mem['3'] = ['d', 'e', 'f']
    mem['4'] = ['g', 'h', 'i']
    mem['5'] = ['j', 'k', 'l']
    mem['6'] = ['m', 'n', 'o']
    mem['7'] = ['p', 'q', 'r', 's']
    mem['8'] = ['t', 'u', 'v']
    mem['9'] = ['w', 'x', 'y', 'z']
    output = ['']
    for number in str:
        letters = mem[number]
        currentArr = []
        for letter in letters:
            for word in output:
                currentArr += [word+letter]
        output = currentArr
    return output

letterCombination("234")