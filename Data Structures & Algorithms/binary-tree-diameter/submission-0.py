# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def depth(node):
            if not node:
                return 0 
            leftDepth = depth(node.left)
            rightDepth = depth(node.right)
            self.res = max(self.res, leftDepth +rightDepth)
            return max(leftDepth , rightDepth) +1
        depth(root)
        return self.res
        

        