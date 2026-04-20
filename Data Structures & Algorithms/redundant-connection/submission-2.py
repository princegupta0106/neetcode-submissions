class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        useless = []
        nodes = {}
        visited = set()
        def find(x):
            if nodes[x] != x:
                nodes[x] = find(nodes[x])
            return nodes[x]
       
        for n1, n2 in edges:
            
            if n1 in visited and n2 not in visited :
                nodes[n2] = nodes[n1]
            elif n2 in visited and n1 not in visited :
                nodes[n1]= nodes[n2]
            elif n1 not in visited and n2 not in visited :
                nodes[n2] = n1
                nodes[n1]= n1
                
            else: 
                # dono hai wala case
                temp1 = find(n1)
                temp2 = find(n2)

                if temp1 == temp2:
                    useless = [n1, n2]
                else:
                    nodes[temp2] = temp1
            visited.add(n1)
            visited.add(n2)
            
        return useless
            

        