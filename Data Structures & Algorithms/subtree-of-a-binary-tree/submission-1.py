# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        def isSame(p ,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val : return False
            if not isSame(p.left , q.left) or not isSame(p.right, q.right):
                return False
            return True
        
        if isSame(root , subRoot): return True
        if  self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        return False
        

        