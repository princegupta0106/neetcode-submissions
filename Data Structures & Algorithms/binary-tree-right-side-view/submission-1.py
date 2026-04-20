# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) :
        # we will do the level order traversal and then for each of them take only the last one 
        if not root : return []
        q = deque()
        res = []
        q.append(root)
        while q:
            level = 0
            temp = []
            for node in q:
                level  = node.val
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            q= temp
            res.append(level)
        return res
