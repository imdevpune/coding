'''
703. Kth Largest Element in a Stream

https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.
 

Example 1:

Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

Output: [null, 4, 5, 5, 8, 8]

Explanation:

KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3); // return 4
kthLargest.add(5); // return 5
kthLargest.add(10); // return 5
kthLargest.add(9); // return 8
kthLargest.add(4); // return 8

Example 2:

Input:
["KthLargest", "add", "add", "add", "add"]
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

Output: [null, 7, 7, 7, 8]

Explanation:

KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
kthLargest.add(2); // return 7
kthLargest.add(10); // return 7
kthLargest.add(9); // return 7
kthLargest.add(9); // return 8
 

Constraints:

0 <= nums.length <= 104
1 <= k <= nums.length + 1
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.


'''
import heapq
from typing import List

#Time Complexity: 
# - __init__(): O(n log n) where n = len(nums)
# - add(): O(log k) where k is the kth largest element to track
#Space Complexity: O(k) for maintaining the min-heap of size k
# Total Time Complexity: O(n log n)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.k=k
        self.nums=nums

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        arr = heapq.nlargest(self.k,self.nums)
        return(arr[self.k-1])


# Without using nlargest(). Just maintain a min-heap of size k by popping smallest elements when size exceeds k.
# Time Complexity: 
# - __init__(k, nums): O(n log n) where n = len(nums). Why:
#   - heapify(nums): O(n)
#   - Popping (n-k) elements: O((n-k) * log n)
# - add(val): O(log k) where k is the parameter
# Total Time Complexity: O(n log n) 

# Space Complexity: O(k) for maintaining the min-heap of size k
#
# Note: After initialization, each add() operation is efficient at O(log k)
# The one-time initialization cost is O(n log n) but subsequent operations are fast
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.k=k
        self.nums=nums
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        while(len(self.nums)>self.k):
            heapq.heappop(self.nums)
        return self.nums[0] 

'''
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

s= KthLargest(3, [4, 5, 8, 2])
print(s.add(3)) # return 4
print(s.add(5)) # return 5
print(s.add(10)) # return 5
print(s.add(9)) # return 8
print(s.add(4)) # return 8  
