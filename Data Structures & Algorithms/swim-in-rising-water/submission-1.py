class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # cost  , i,j
        minHeap = [[grid[0][0] , 0,0]]
        m = len(grid)
        n = len(grid[0])
        i ,j  = 0, 0
        visited =set()
        cost  = 0 
        while True :
            cost  , i,j = heapq.heappop(minHeap)
            if i ==m-1 and j == n-1 :
                break 
            if (i,j) in visited:
                continue
            visited.add((i,j))
            if i > 0 :
                heapq.heappush(minHeap ,(max(cost , grid[i-1][j]) , i-1 , j))
            if j > 0 :
                heapq.heappush(minHeap ,(max(cost , grid[i][j-1]) , i , j-1 ))
            if i < m-1:
                heapq.heappush(minHeap ,(max(cost , grid[i+1][j]) , i +1 , j))
            if j < n-1 :
                heapq.heappush(minHeap ,(max(cost , grid[i][j+1]) , i , j+1))
        return cost 


