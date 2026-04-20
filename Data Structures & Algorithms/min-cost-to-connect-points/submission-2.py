class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        minHeap = [[0,0]] # cost , point index 
        total_cost = 0
        while len(visited) < n:
            cost , i  = heapq.heappop(minHeap)
            
            if i in visited:
                continue
            visited.add(i)
            total_cost += cost
            for j in range(n):
                if j not in visited:
                    x1,y1 = points[i]
                    x2,y2= points[j]
                    distance = abs(x1-x2) +abs(y1-y2)
                    heapq.heappush(minHeap, (distance , j))
        return total_cost