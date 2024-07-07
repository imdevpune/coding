'''
https://leetcode.com/problems/course-schedule/description/
https://www.youtube.com/watch?v=WAOfKpxYHR8

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

'''
import collections
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=collections.defaultdict(list)
        indegree = [0] * numCourses
  
        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v]+=1


        '''
        for current in graph:
            for neighbour in graph[current]:
                indegree[neighbour]+=1
        '''
        print(f"indegree = {indegree}")

        
        q = collections.deque()
        for index,value in  enumerate(indegree):
            if value == 0 :
                q.append(index)

        topo_sort = []
        while(q):
            current = q.popleft()
            topo_sort.append(current)
            for neighbour in graph[current]:
                indegree[neighbour]-=1
                if indegree[neighbour] == 0:
                    q.append(neighbour)

        print(f"topo_sort = {topo_sort}")

        return len(topo_sort) == numCourses




        ''' DFS way 
        d = collections.defaultdict(list)
        for k,v in prerequisites:
            d[k].append(v)

        visited = set()

        def dfs(cor):
            if cor in visited:
                return False
            if d[cor]==[]:
                return True
            visited.add(cor)

            for c in d[cor]:
                if not dfs(c):
                    return False
            d[cor]=[]
            visited.remove(cor)
            return True

        for n in range(numCourses):
            if dfs(n) == False:
                return False
        return True
        '''


s = Solution()
prerequisites = [[1,0]]
print(s.canFinish(2,prerequisites))

prerequisites1 = [[1,0],[0,1]]
print(s.canFinish(2,prerequisites1))
