class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #making the graph 
        
        graph = defaultdict(list)
        for (src, dst) in sorted(tickets ,reverse = True) :
            graph[src].append(dst)
        
        
        # using edge only once algorithm 
        path = []
        def dfs(node):
            
            while graph[node]:
                nei = graph[node].pop()
                dfs(nei)
            path.append(node)
        dfs("JFK")

        return path[::-1]

        

        

        