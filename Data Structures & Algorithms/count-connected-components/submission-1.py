class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        count = 0
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei in visited:
                    continue
                dfs(nei)
        for key in graph.keys():
            if key not in visited:
                dfs(key)
                count +=1 
        if len (visited) == n :

            return count 
        else :
            return count + n-len(visited)

        
                
            


        