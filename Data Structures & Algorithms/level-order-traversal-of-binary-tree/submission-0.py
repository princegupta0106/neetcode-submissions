# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l = []
        l.append(root)
        if not root : return []
        res = [[root]]
        while l: 
            temp  = []
            for node in l:
                if node: 
                    if node.left: temp.append(node.left)
                    if node.right: temp.append(node.right)
            res.append(temp)
            l = temp
       
        if not res : return res
        for i in range(len(res)):
            for j in range(len(res[i])):
                res[i][j] = res[i][j].val
        return res[:len(res)-1]
                
        
        