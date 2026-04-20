class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # make a graph first 
        graph = defaultdict(list)
        n =len(tickets)
        # here we are not using reverse= True because we are not popping the nodes we are checking all of them with a for loop 
        for (src, dst) in sorted(tickets):
            graph[src].append(dst)
        
        # make a ticket usage couter 
        usage = defaultdict(int)
        for ticket in tickets:
            usage[tuple(ticket)] += 1 
        # we  have set all the edges usage to 1 now 
        path  = ['JFK']    

        def dfs(node) :
            if len(path) == n + 1:
                return True
   
            for nei in graph[node]:
                if usage[(node , nei)] > 0 :
                    usage[(node , nei)] -= 1
                    path.append(nei)
                    if dfs(nei) :
                        return True
                    path.pop()
                    usage[(node , nei)] += 1
            return False 
        dfs('JFK')
        return path


