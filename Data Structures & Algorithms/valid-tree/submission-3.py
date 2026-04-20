class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = defaultdict(list)
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        q = deque([(0, -1)])   # (node, parent)
        while q:
            node, parent = q.popleft()
            visited.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False   # cycle detected
                q.append((nei, node))   # pass parent properly
        if len(visited)!= n : return False
        return True
            
            
        
             

      



            
            

          