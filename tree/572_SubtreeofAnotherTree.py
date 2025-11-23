'''
572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/description/

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

Time Complexity: O(N*M) where N is number of nodes in tree 'root' and M is number of nodes in tree 'subRoot'. In worst case, for each node in 'root', we may have to compare all nodes in 'subRoot'.
Space Complexity: O(H1 + H2) where H1 and H2 are heights of trees 'root' and 'subRoot' respectively due to recursive stack space.

'''

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True
        if root == None:
            return False
        # if root.val == subRoot.val:
        #     if self.isSameTree(root,subRoot) == True:
        #         return True
        if self.isSameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
s = Solution()
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)   
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2) 

print(s.isSubtree(root, subRoot))
