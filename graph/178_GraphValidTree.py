'''
https://www.lintcode.com/problem/178/

Description
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Only $39.9 for the "Twitter Comment System Project Practice" within a limited time of 7 days!

WeChat Notes Twitter for more information（WeChat ID jiuzhangfeifei）


You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example
Example 1:

Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.
Example 2:

Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.
'''
import collections
from typing import List

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if not edges:
            return True
        
        visited = set()
        graph = collections.defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
      
        def dfs(i,prev):
            if i in visited:
                return False
            visited.add(i)
            
            for neighbour in graph[i]:
                if neighbour == prev:
                    continue
                if neighbour in visited:
                    return False
                if not dfs(neighbour,i):
                    return False
            return True
                
        return dfs(0,-1) and len(visited)==n
                

s = Solution()
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(s.valid_tree(5,edges))

edges1 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print(s.valid_tree(5,edges1))
