'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted container. 
If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Input: nums = [1,2,3]
Output: [1,3,2]

Input: nums = [3,2,1]
Output: [1,2,3]

Input: nums = [1,1,5]
Output: [1,5,1]
'''
def nextPermutation(nums):
    # recursion 

    # function 1, check if given list is decending (ex: [3, 2, 1])
    def isDescending(list): 
        reverseList = sorted(list, reverse=True)
        if list == reverseList:         # return true if it is decending 
            return True
        else:                           # else return false
            return False

    # function 2 change the head        
    def changeHead(head, nums): 
        nums.insert(0, head)    # add the head back into nums
        nums.sort()             # sort the head
        for i, num in enumerate(nums):  # enumerate through nums
            if num > head:              # if current num is greater than head
                head = num              # set new head as current num
                nums.pop(i)             # pop the current num from nums
                break                   # break out of for loop
        nums.insert(0, head)            # insert the head to the front of nums
        return

    # function 3 simply switches the last two values in nums
    def switch(nums):
        temp = nums.pop()
        nums.insert(0, temp)
        return

    # the basic logic is we use recursion until there are only 2 values in nums or it is decending 
    if isDescending(nums):  # if nums is decending return the sorted nums
        nums.sort() 
        return
    else:                   # otherwise move on
        head = nums.pop(0)      # save the first value of num as head
        if isDescending(nums):  # if the remaining values in nums is decending 
            changeHead(head, nums)      # change the head into the next value and put it in front 
                                        # changeHead already insert back head so we can return
            return
        elif len(nums) == 2:        # if nums is left with two values that are in ascending 
            switch(nums)            # use switch function to switch the values
            nums.insert(0, head)    # insert back head
            return
        else:
            nextPermutation(nums)       # this is where recursion is, we will pop the head until 
            nums.insert(0, head)        # final insert back head after recursion
            return
        
        
nums = [2,2,7,5,4,3,2,2,1]
nextPermutation(nums)
print(nums)
