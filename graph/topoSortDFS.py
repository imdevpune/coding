import collections
from typing import List


class TopoSortDFS:
    def topoSort(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def topo_dfs(n):
            for i in graph[n]:
                if i not in visited:
                    topo_dfs(i)
            visited.add(n)
            q.append(n)


        # create dictionary from list
        graph = collections.defaultdict(list)
        # graph= {c:[] for c in range(numCourses)}
        # print(f" ------- {graph}")
        for u,v in prerequisites:
            graph[u].append(v)
        print(graph)
        
       
        visited = set()
        q = collections.deque()
        for node in range(numCourses):
            if node not in visited:
                topo_dfs(node)
                
            
        # print toplogical order 
        topo=[]
        while(q):
            topo.append(q.pop())
        print(topo)    
            



s = TopoSortDFS()

pre = [[5,2],[5,0],[4,0],[4,1] ,[2,3],[3,1]]
print(s.topoSort(6,pre))
