'''
https://leetcode.com/problems/number-of-provinces/description/

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
'''

from collections import defaultdict
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size=len(isConnected)
        par=[i for i in range(len(isConnected))]
        rank =[1] * len(isConnected)

        def find(n1):
            res=n1
            while res!= par[res]:
                par[res]=par[par[res]]  #path compression
                res=par[res]
            return res
        
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            
            if p1 == p2:
                return 0
            if rank[n2]>rank[n1]:
                par[n1]=n2
                rank[n2] = rank[n2] + rank[n1]
            else:
                par[n1]=n2
                rank[n1] = rank[n1] + rank[n2]
            return 1
        
        result=len(isConnected)
        for i in range(size):
            for j in range(size):
                if isConnected[i][j] == 1:
                    result-=union(i,j)
        print(f"result={result}")
        
s = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
s.findCircleNum(isConnected)

isConnected1 = [[1,0,0],[0,1,0],[0,0,1]]
s.findCircleNum(isConnected1)
