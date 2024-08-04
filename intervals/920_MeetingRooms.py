'''
https://www.lintcode.com/problem/920/
Description
Given an array of meeting time intervals consisting of start and end times [(s1,e1),(s2,e2),...] (si < ei), determine if a person could attend all meetings.

Example1
0≤intervals.length≤10^4
intervals[i].length==2
[(0,8), (8,10)] is not conflict at 8

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict
Example2

Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 

'''
from typing import List




class Solution:

    class Interval(object):
        def __init__(self, start, end):
            self.start = start
            self.end = end
    # def can_attend_meetings(self, intervals: List[Interval]) -> bool:
    #     # Write your code here
    #     for i in range(len(intervals)):
    #         for j in range(i+1,len(intervals)):
    #             if(intervals[i].end > intervals[j].start):
    #                 return False
    #     return True
    
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        print(type(intervals[0]))
        intervals.sort(key=lambda i: i.start)
        for i in range(len(intervals)):
            if(intervals[i-1].end > intervals[i].start):
                return False
        return True
        

s = Solution()
i = s.Interval(0, 30)
j = s.Interval(5, 10)
k = s.Interval(15, 20)
intervals = [i, j, k]
#intervals = [(0,30),(5,10),(15,20)]
print(s.can_attend_meetings(intervals))  # False

intervals = [(5,8),(9,15)]
print(s.can_attend_meetings(intervals))  # True
