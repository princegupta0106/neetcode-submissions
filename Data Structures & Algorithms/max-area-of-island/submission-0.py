class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea =  0 
        m = len(grid)
        n = len(grid[0])
        def dfs(i, j):
            if i == m or j == n or i < 0 or  j < 0 or grid[i][j] == 0:
                return 0 
            res = 1
            grid[i][j] = 0
            res += dfs(i+1 , j)
            res += dfs(i,j+1)
            res += dfs(i-1,j)
            res += dfs(i,j-1)
            return res 

        for i in range(m):
            for j in range(n):
                if grid[i][j] :
                    maxarea = max(maxarea, dfs(i,j))
        return maxarea