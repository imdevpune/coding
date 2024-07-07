
'''
https://leetcode.com/problems/course-schedule-ii/
https://www.youtube.com/watch?v=WAOfKpxYHR8
https://takeuforward.org/data-structure/course-schedule-i-and-ii-pre-requisite-tasks-topological-sort-g-24/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]


Time Complexity: O(V+E), where V = no. of nodes and E = no. of edges. This is a simple BFS algorithm.
Space Complexity: O(N) + O(N) ~ O(2N), O(N) for the indegree array, and O(N) for the queue data structure used in BFS(where N = no.of nodes). Extra O(N) for storing the topological sorting. Total ~ O(3N).

'''


import collections
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = [0] * numCourses

        for u,v in prerequisites:
            #graph[u].append(v)
            graph[v].append(u)
            #indegree[v]+=1
            indegree[u]+=1
        print(f"indegree = {indegree}")

        q = collections.deque()
        for index,value in enumerate(indegree):
            if value == 0:
                q.append(index)


        topo_order = []
        while(q):
            current = q.popleft()
            topo_order.append(current)
            for neighbour in graph[current]:
                indegree[neighbour]-=1
                if(indegree[neighbour]==0):
                    q.append(neighbour)

        print(f"topo_order = {topo_order}")
        if len(topo_order) == numCourses:
            return topo_order
        else:
            return []




s = Solution()
prerequisites = [[1,0]]
print(s.findOrder(2,prerequisites))

prerequisites1 = [[1,0],[0,1]]
print(s.findOrder(2,prerequisites1))
