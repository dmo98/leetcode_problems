# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS approach
        # base case -> empty tree
        # recurrence relation -> minDepth(root) = 1 + min(minDepth(root.left) ,minDepth(root.right))
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        # deals with the case where one of the subtrees is None. It shouldn't contribute to the minDepth based on the definition of minDepth in the problem
        if min(left, right) != 0:
            return 1 + min(left, right)
        else:
            return 1 + max(left, right)
        