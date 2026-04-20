# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minimum  = float('inf')
        maximum = float('-inf')
        def dfs(node , minimum , maximum):
            if not node :  return True
            if node.val <= maximum or node.val >= minimum: 
                return False
            
            return dfs(node.left ,min(minimum , node.val) , maximum) and dfs(node.right ,minimum , max(maximum , node.val))
        return dfs(root , minimum , maximum)

        