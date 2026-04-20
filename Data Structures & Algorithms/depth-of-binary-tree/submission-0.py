# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q= deque()
        q.append((root , 1))
        maxRank = 0
        while q:

            node, rank  =q.popleft()
            if not node :
                continue 
            maxRank = max(rank ,maxRank)
            
            q.append((node.left , rank+1) )
            q.append((node.right , rank+1) )
        return maxRank


        