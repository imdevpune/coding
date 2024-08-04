'''
https://leetcode.com/problems/insert-interval/description/
https://www.youtube.com/watch?v=xxRE-46OCC8

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.
Note that you don't need to modify intervals in-place. You can make a new array and return it.


Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        size = len(intervals)
        i=0
        
        # Add all intervals in result till you find overlapping condition
        while(i < size and intervals[i][1] < newInterval[0]):
            res.append(intervals[i])
            i+=1
            
        # Merge all intervals that overlap with newInterval
        # Execute this loop till newInterval[1] is greater than intervals[i][0]. e.g in 2nd example,we will keep merging [4,8] until we found [12,16]
        while(i<size and intervals[i][0] <= newInterval[1]):
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
            i+=1
        res.append(newInterval)
        
        # put all remaining intervals as it is
        while(i<size):
            res.append(intervals[i])
            i+=1
            
        return res
        
        
s = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(s.insert(intervals, newInterval))  # [[1,5],[6,9]]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] 
newInterval = [4,8]
print(s.insert(intervals,newInterval)) 
