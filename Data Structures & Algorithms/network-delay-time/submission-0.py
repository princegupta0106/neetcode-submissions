from collections import defaultdict 
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        visited = set()
        for (u,v,t) in times :
            graph[u].append((v,t))
        
        maxTime = 0
        #initial time and node
        q = [(0,k)]

        while q:
            time , node = heapq.heappop(q)
            if node in visited:
                continue
            maxTime = time
            visited.add(node)
            for (nei,t) in graph[node]:
                if nei in visited:
                    continue
                heapq.heappush(q , (time+t , nei))
        return maxTime if len(visited) ==n else -1



        

            

            


        



        