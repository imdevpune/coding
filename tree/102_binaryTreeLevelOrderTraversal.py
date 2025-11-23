'''
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

Constraints: 
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

Time Complexity: O(N) where N is number of nodes in tree. Why: because we visit each node exactly once.
Space Complexity: O(W) where W is maximum width of the tree. In worst case, W can be N/2 for a balanced tree.
'''

from typing import List, Optional
import collections
from unittest import result
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return [root]
        
        result = []
        q = collections.deque()
        q.append(root)

        while q:
            arr = []
            size = len(q)
            
            for i in range(size):
                ele = q.popleft()
                if ele.left:
                   q.append(ele.left)
                if ele.right:
                   q.append(ele.right)
                arr.append(ele.val)
            result.append(arr)
        return result

s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

res = s.levelOrder(root)
print(res)
