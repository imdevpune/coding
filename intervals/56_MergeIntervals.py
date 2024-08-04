'''
https://leetcode.com/problems/merge-intervals/description/
https://www.youtube.com/watch?v=2JzRBPFYbKE&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=7

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

'''

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        result=[]
        temp=intervals[0]
        for i in range(1,len(intervals)):
            if temp[1] >= intervals[i][0]:
                temp[1] = max(temp[1],intervals[i][1])
            else:
                result.append(temp)
                temp=intervals[i]
        result.append(temp)
        return result
    
s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18],[0,3]] 
print(s.merge(intervals)) #[[1,6],[8,10],[15,18]]

intervals = [[1,4],[4,5]]
print(s.merge(intervals)) #[[1,5]]
  
intervals = [[1,2],[3,5],[4,6],[6,7],[8,10],[12,16]]
print(s.merge(intervals)) #[[1,2],[3,7],[8,10],[12,16]]

intervals=[[1,4],[5,6],[0,3]]
print(s.merge(intervals)) #[[0,4],[5,6]]
'''
sorting complexity = O(n log n)
for loop complexity = O(n)
Total complexity = O(n log n) + o(n) = O(n log n)

Space complexity = O(n) for result
'''
