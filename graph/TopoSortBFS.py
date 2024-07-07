import collections
from typing import List

'''
Topological Sort Algorithm - BFS | Kahn's Algorithm | 
https://takeuforward.org/data-structure/kahns-algorithm-topological-sort-algorithm-bfs-g-22/
'''
class TopoSortBFS:
    def topoSort(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses
        
        # create dictionary from list
        graph = collections.defaultdict(list)
        # graph= {c:[] for c in range(numCourses)}
        # print(f" ------- {graph}")
        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v]+=1 # instead of having one more loop to calculate indegree, we can caculate here
        print(graph)
        
        '''
        # Iterate over graph and calculate indegree of each node
        # [0,1] means there is edge from 0 to 1. So indegree[1]=1
        for n in graph:
            for i in graph[n]:
                indegree[i]+=1
        '''
        print(f"indegree = {indegree}")


        # Initialize deque and add all vertices with in-degree 0
        q = collections.deque()
        for index,value in enumerate(indegree):
            if(value == 0):
                q.append(index)


        '''
        While the queue is not empty:
        Remove a vertex 'current' with in-degree 0 from the queue and add it to topo_order.
        For each neighbor of current, decrement its in-degree by 1. If a neighbor's in-degree becomes 0, add it to the queue.
        '''
        topo_order=[]
        while(q):
            # Remove a vertex with in-degree 0
            current = q.popleft()
            topo_order.append(current)
            
            # Decrease in-degree of its neighbors
            for neighbor in graph[current]:
                indegree[neighbor]-=1
                if(indegree[neighbor]==0):
                    q.append(neighbor)
                  


        # Check if there was a cycle in given graph
        # if length of 'topo_order' is equal to orinal vertces then there is no cycle
        if len(topo_order) == len(indegree):
            return topo_order
        else:
            # Return an empty list if there is a cycle
            print("cycle in graph")
            return []


s = TopoSortBFS()
pre = [[5,2],[5,0],[4,0],[4,1] ,[2,3],[3,1]]
print(s.topoSort(6,pre))

'''
All Possible topological orders are as below 
[4, 5, 2, 3, 1, 0]
[4, 5, 2, 3, 0, 1]
[4, 5, 2, 0, 3, 1]
[4, 5, 0, 2, 3, 1]
[5, 4, 2, 3, 1, 0]
[5, 4, 2, 3, 0, 1]
[5, 4, 2, 0, 3, 1]
[5, 4, 0, 2, 3, 1]
'''
