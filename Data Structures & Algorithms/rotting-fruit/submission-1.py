class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m  = len(grid)
        n = len(grid[0])
        res = 0
        mark  = [[float('inf')]*n for _ in range (m)]


        def dfs(i , j , time):
            if i <0 or j < 0 or i ==m or j == n or grid[i][j] == 0:
                return 
            if time >= mark[i][j]:
                return 
            mark[i][j] = time 
            # grid[i][j] = 2 
            dfs(i, j+1, time+1)
            dfs(i, j-1, time+1)
            dfs(i+1, j, time+1)
            dfs(i-1, j, time+1)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dfs( i, j , 0)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and mark[i][j] == float('inf'):
                    return -1
                if grid[i][j] != 0 and mark[i][j] != float('inf'):
                    res = max(res, mark[i][j])
        return res