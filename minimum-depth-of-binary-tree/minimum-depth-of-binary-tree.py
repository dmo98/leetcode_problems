# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive helper function: 
        # base case -> empty tree, leaf
        # recurrence relation -> minDepth(root) = 1 + min(minDepth(root.left) ,minDepth(root.right))
        def minDepthHelper(node, current_minimum):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            left = minDepthHelper(node.left, current_minimum + 1)
            right = minDepthHelper(node.right, current_minimum + 1)
            
            if min(left, right) != 0:
                return 1 + min(left, right)
            else:
                return 1 + max(left, right)
        
        return minDepthHelper(root, 0)
        