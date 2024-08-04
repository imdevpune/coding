'''
https://leetcode.com/problems/jump-game/description/
https://www.youtube.com/watch?v=tZAa_jJ3SwQ

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 
Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105
'''

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        goal=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal=i
        
        return True if goal==0 else False
        '''
        max_index = 0
        for i in range(len(nums)):
            # If the current index is greater
            # than the maximum reachable index
            # it means we cannot move forward
            # and should return false
            if i > max_index:
                return False

            # Update the maximum index
            # that can be reached by comparing
            # the current max_index with the sum of
            # the current index and the
            # maximum jump from that index
            max_index = max(max_index, i + nums[i])

s = Solution()
nums = [2,3,1,1,4]
#print(s.canJump(nums))  # True

nums = [3,2,1,0,4]  
print(s.canJump(nums))  # False

nums = [1,1,0,2,1] 
print(s.canJump(nums))  # False
