'''
https://www.lintcode.com/problem/919/
https://aaronice.gitbook.io/lintcode/sweep-line/meeting-rooms-ii
https://www.youtube.com/watch?v=FdzJmTCVyJU

Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), find the minimum number of conference rooms required.

Example 1:
Input:
[[0, 30],[5, 10],[15, 20]]
Output:
 2
 
Example 2:
Input:
 [[7,10],[2,4]]

Output:
 1
'''
'''
time complexity 
sorting = O(n log n)
for loop = O(n)
Total = O(n log n)

Space complexity = O(n) for start and end
'''

from typing import List
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        # intervals.sort(key=lambda x:x.start)

        result,count=0,0
        endIndex=0
        
        for i in range(len(start)):
            if start[i] < end[endIndex]:
                count+=1
            else:
                endIndex+=1
                count-=1
            result=max(result,count)
        return result

s = Solution()
intervals = [Interval(0,30),Interval(5,10),Interval(15,20)]
# intervals = [Interval(0,30),Interval(5,10),Interval(15,20),Interval(2,10)]
#intervals = [[0, 30],[5, 10],[15, 20]]
print(s.min_meeting_rooms(intervals)) #2

intervals = [Interval(7,10),Interval(2,4)]
print(s.min_meeting_rooms(intervals)) #1
