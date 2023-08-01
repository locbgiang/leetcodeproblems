'''
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
'''

def combinationSum2(candidates, target):
    def dfs(candidates, target, path, answer):
        if target == 0:
            path.sort()
            if path not in answer:
                answer.append(path)
            return
        for i in range(len(candidates)):
            if candidates[i] > target:
                continue
            if i>=1 and candidates[i]==candidates[i-1]:
                continue
            dfs(candidates[i+1:], target-candidates[i], path+[candidates[i]], answer)
        return 

    answer = []
    dfs(candidates, target, [], answer)
    return answer

candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(candidates, target))