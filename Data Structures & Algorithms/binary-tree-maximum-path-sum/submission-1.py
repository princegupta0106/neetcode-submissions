# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -10000
        def dfs(node):
            if not node : return 0 
            nonlocal res
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, node.val ,node.val+left , node.val+right , left+right+node.val )
            return max(node.val , node.val+left , node.val+right)
        dfs(root)
        return res
        