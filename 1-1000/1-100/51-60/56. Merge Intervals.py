'''
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    answer = [intervals[0]]
    for i in range(1, len(intervals)):
        curInterval = intervals[i]
        lastInterval = answer[-1]
        if curInterval[0] <= lastInterval[1]:
            lastInterval[1] = max(curInterval[1], lastInterval[1])
        else:
            answer.append(curInterval)
    return answer

intervals = [[2,3],[4,5],[6,11],[8,9],[1,10]]
merge(intervals)