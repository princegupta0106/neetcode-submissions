class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0 
        visited  = set()
        drxn  = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    q = deque() 
                    q.append((i,j))
                    while q:
                        a,b = q.pop()
                        visited.add((a,b))
                        
                        for r,c in drxn:
                            x , y  = r+a , c+b 
                            if x >=0 and x < m and y >= 0 and y < n and grid[x][y]== '1' and  (x,y) not in visited:
                                q.append((x,y))
                    res += 1
        return res 
            







