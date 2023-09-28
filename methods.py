def topKFrequent(): # leetcode 347
    mem = {}
    for i in nums:
        # dictionary set if does not exist
        mem[i] = 1 + mem.setdefault(i, 0)
    #returning all list inside mem  
    return [sorted(mem.items(), key = lambda x:-x[1])[i][0] for i in range(0, k)]

nums = [2,3,4,1,4,0,4,-1,-2,-1]
k = 2
p = topKFrequent(nums, k)
print('dictionary')

def ifelse():
    # 1 line if else
    age_group = "Minor" if age < 18 else "Adult"
    # regular 
    age = 20    
    if age < 18:
        age_group = "Minor"
    else:
        age_group = "Adult"