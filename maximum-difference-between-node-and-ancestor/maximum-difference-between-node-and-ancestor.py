# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # Recursive helper function:
        # base case -> empty tree, leaf node
        # recurrence relation -> maxAncestorDiff(root) = max(max(maxLeft, root.val) - min(minLeft, root.val), max(maxRight, root.val) - min(minRight, root.val)
        def maxAncestorDiffHelper(node, minVal, maxVal):
            if node is None:
                return 0
            
            minVal = min(minVal, node.val)
            maxVal = max(maxVal, node.val)
            if node.left is None and node.right is None:
                return abs(maxVal - minVal)
            
            left = maxAncestorDiffHelper(node.left, minVal, maxVal)
            right = maxAncestorDiffHelper(node.right, minVal, maxVal)
            return max(left, right)
            
        
        return maxAncestorDiffHelper(root, root.val, root.val)
        