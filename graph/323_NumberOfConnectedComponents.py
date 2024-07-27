'''
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

https://www.youtube.com/watch?v=8f1XPm4WOUc

Number of Connected Components in an Undirected Graph
 Description
In this problem, there is an undirected graph with n nodes. There is also an edges array. Where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.
You need to return the number of connected components in that graph.

Example
Input:
3
[[0,1], [0,2]]
Output:
1

Input:
6
[[0,1], [1,2], [2, 3], [4, 5]]
Output:
2
'''

from typing import List

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        size = n
        rank = [1] * size
        par = [i for i in range(size)]
        
        def find(n1):
            res=n1
            while res!= par[res]:
                par[res]=par[par[res]]   #path compression
                res=par[res]
            return res
        
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p2]>rank[p1]:
                par[p1]=p2
                rank[p2] = rank[p2] + rank[p1]
            else:
                par[p2]=p1
                rank[p1] = rank[p1] + rank[p2]
            return 1
        
        result=size
        for e1,e2 in edges:
            result-=union(e1,e2)
            
        return result
    
    
s = Solution()
edges1 = [[0,1], [0,2]]
print(s.count_components(3,edges1))

edges2 = [[0,1], [1,2], [2, 3], [4, 5]]
print(s.count_components(6,edges2))
