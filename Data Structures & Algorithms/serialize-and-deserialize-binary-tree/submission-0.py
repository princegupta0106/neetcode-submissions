# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node):
            if not node: return [None]
            return [node.val]+ dfs(node.left) +dfs(node.right)
        string = str(dfs(root))
        return string[1:len(string)-1]

            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(', ')
        for i in range(len(arr)) :
            if arr[i] == "None":
                arr[i] = None
            else :
                arr[i] = int(arr[i])
        arr = deque(arr)
        def dfs():
            val = arr.popleft()
            if not val: return None
            node = TreeNode(val)
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        
            
