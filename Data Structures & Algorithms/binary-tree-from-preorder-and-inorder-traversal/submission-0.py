# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexes = { val: idx for idx , val in enumerate(inorder)}
        preidx = 0
        def dfs(left , right):
            nonlocal preidx
            
            if left > right :
                return None
            rootval = preorder[preidx]
            mid  = indexes[rootval]
            preidx += 1
            node = TreeNode(rootval)
            node.left   = dfs(left , mid-1)
            node.right = dfs(mid+1  , right)
            return node
        return dfs(0, len(preorder)-1)

            




        