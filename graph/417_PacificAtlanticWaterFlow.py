'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


'''

from typing import List


def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    ROWS = len(heights)
    COLS = len(heights)
    pacVisit, atalVisit = set() , set()
    
    def dfs(r,c,visit,prevHeight):
        print(f"(r,c)={(r,c)}")
        if r<0 or c<0 or r==ROWS or c==COLS or heights[r][c]<prevHeight or (r,c) in visit:
            return
        
        visit.add((r,c))
        dfs(r-1,c,visit,heights[r][c])
        dfs(r+1,c,visit,heights[r][c])
        dfs(r,c-1,visit,heights[r][c])
        dfs(r,c+1,visit,heights[r][c])
        
        
    for r in range(ROWS):
        dfs(r,0,pacVisit,heights[r][0])
        dfs(r,COLS-1,atalVisit,heights[r][COLS-1])
        
    for c in range(COLS):
        dfs(0,c,pacVisit,heights[0][c])
        dfs(ROWS-1,c,atalVisit,heights[ROWS-1][c])
        
    result = []
    for i in range(ROWS):
        for j in range(COLS):
            if (i,j) in atalVisit and (i,j) in pacVisit:
                result.append((i,j))
        
    return result



heights1 =[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
#print(pacificAtlantic(any,heights1))
# expected output = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

heights2 =[[1,1],[1,1],[1,1]]
print(pacificAtlantic(any,heights2))
