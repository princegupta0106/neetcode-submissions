class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        useless = []
        component  = {}
        nodes = {}
        visited = set()
       
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
                temp1 = n1
                while nodes[temp1] != temp1:
                    temp1 = nodes[temp1]
                temp2 = n2
                while nodes[temp2] != temp2:
                    temp2 = nodes[temp2]
                if temp1 == temp2:
                    useless= [n1,n2]
                else:
                    nodes[temp2] = temp1
            visited.add(n1)
            visited.add(n2)
            
        return useless
            

        