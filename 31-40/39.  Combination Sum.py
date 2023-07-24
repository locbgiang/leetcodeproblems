'''
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
'''
def combinationSum(candidates, target):
    def DepthFirstSearch(candidates, target, path, answer):
        if target == 0:
            answer.append(path)
            return
        for i in range(len(candidates)):
            if candidates[i] > target:
                continue
            print(path+[candidates[i]])
            DepthFirstSearch(candidates[i:], target-candidates[i], path+[candidates[i]], answer)
    
    answer = []
    DepthFirstSearch(candidates, target, [], answer)
    return answer

    
candidates = [7,3,2]
target = 18
print(combinationSum(candidates, target))

'''
for i in candidates:
            if sum(temp)+i < target:
                temp.append(i)
                addTree(temp, answer)
            elif sum(temp)+i > target:
                temp.pop(0)
                return 
            else:
                temp.append(i)
                temp.sort()
                if temp not in answer:
                    print('found ', temp)
                    answer.append(temp)
                return 
        return
'''