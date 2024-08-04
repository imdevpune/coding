
'''
https://leetcode.com/problems/maximum-subarray/description/
https://www.youtube.com/watch?v=5WZl3MMT0Eg

53. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
 
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxi=nums[0]
        
        for n in nums:
            sum+=n
            maxi=max(maxi,sum)
            if(sum<0):
                sum=0
        return maxi
        
        
        
s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))  # 6

nums = [5,4,-1,7,8]
print(s.maxSubArray(nums))  # 23

nums = [1]
print(s.maxSubArray(nums))  # 1

nums = [-5,-4,-3,-7,-8]
print(s.maxSubArray(nums))  # -3
