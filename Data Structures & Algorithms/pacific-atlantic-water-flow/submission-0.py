class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific , atlantic = set() , set()
        res  = []
        m = len(heights)
        n =len(heights[0])
        drxn  = [[1,0],[-1,0] , [0,1], [0,-1]]
        def dfs(i, j , prev_h, visited_set):
            if (i,j) in visited_set or i <0 or j < 0 or i == m or j ==n  or heights[i][j] < prev_h:
                return 
            visited_set.add((i,j))
            
            for dx , dy in drxn:
                dfs(i+dx ,j+ dy ,heights[i][j] ,visited_set )
            return 
        
        # for pacific 
        for i in range(m):
            dfs(i,0 , -1 , pacific)
        for j in range(n):
            dfs(0,j , -1,pacific)
        # for atlantic
        for i in range(m):
            dfs(i,n-1 , -1 , atlantic)
        for j in range(n):
            dfs(m-1,j , -1,atlantic)
        
        return list(pacific&atlantic)



        
        