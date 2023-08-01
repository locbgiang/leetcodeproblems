'''
You are given an array of non-overlapping intervals intervals where 
intervals[i] = [starti, endi] represent the start and 
the end of the ith interval and intervals is sorted in ascending order by starti. 

You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and 
intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

# for loop through intervals
# if cur interval end point is less than new start
# append current interval to answer
# else if cur interval start point is greater than end point of newInterval
# append newInterval 
# set newInterval as cur interval
# otherwise set the min and max of newInterval 
def insert(intervals, newInterval):
    answer = []
    for i in intervals:
        if i[1] < newInterval[0]:
            answer.append(i)
        elif i[0] > newInterval[1]:
            answer.append(newInterval)
            newInterval = i
        else:
            newInterval[0] =  min(i[0], newInterval[0])
            newInterval[1] = max(i[1], newInterval[1])
    answer.append(newInterval)
    return answer


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
insert(intervals, newInterval)