'''
https://leetcode.com/problems/non-overlapping-intervals/description/
https://www.youtube.com/watch?v=HDHQ8lAWakY

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:
1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
'''

'''
Time complexity = O(n log n) for sorting
Time complexity = O(n) for for loop
Total time complexity = O(n log n) + O(n) = O(n log n)

Space complexity = O(1)
'''

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[1])
        print(f"intervals={intervals}")
        temp=intervals[0]
        count=1
        for cur in intervals[1:]:
            if temp[1] <= cur[0]:
                count+=1
                temp=cur
        return len(intervals)-count

s=Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(s.merge(intervals)) #1
