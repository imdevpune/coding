'''
200. Number of Islands
https://leetcode.com/problems/number-of-islands/description/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.


Time Complexity:
The time complexity of this solution is O(m * n), where m is the number of rows and n is the number of columns in the grid. In the worst case, we may need to visit every cell in the grid once.
Space Complexity:
The space complexity is O(m * n) in the worst case, which occurs when the grid is filled with land ('1's) and the DFS stack goes as deep as the number of cells in the grid.
'''
from typing import List

class Solution:
    def dfs(self,r:int,c:int,grid:List[List[str]]):
        if (r<0 or c<0 or r>= len(grid) or c >= len(grid[0]) or grid[r][c]=='0' ):
            return
        grid[r][c]='0'
        self.dfs(r-1,c,grid)
        self.dfs(r,c-1,grid)
        self.dfs(r+1,c,grid)
        self.dfs(r,c+1,grid)
        return 1

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=='1':
                    count+=self.dfs(i,j,grid)
        return count


s = Solution()
grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ]
print(s.numIslands(grid))

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(s.numIslands(grid))
