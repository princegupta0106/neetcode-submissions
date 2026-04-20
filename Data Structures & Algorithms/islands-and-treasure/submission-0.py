class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n =len(grid[0])
        def dfs(i , j , distance):
            if i <0 or j < 0 or i== m or j ==n  or grid[i][j] == -1 :
                return 
            if distance > grid[i][j]:
                return
            
            grid[i][j] = distance 
            grid[i][j] = distance
            dfs( i,j+1  , distance+1)
            dfs( i+1,j  , distance+1)
            dfs( i,j-1 , distance+1)
            dfs( i-1,j  , distance+1)
            return 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 :
                    dfs(i,j , 0)
        
            


        