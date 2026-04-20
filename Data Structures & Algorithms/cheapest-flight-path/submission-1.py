class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        minHeap = [(0,src,-1)]
        
        for (f , t, p ) in flights:
            graph[f].append((t , p))
        
        while minHeap:
            cost ,node , stops = heapq.heappop(minHeap)
            
            if node == dst: return cost 
            if stops ==k : continue
            for (nei ,c) in graph[node]:
                heapq.heappush( minHeap , (cost+c  ,nei , stops+1 ))
     
        return -1 


        