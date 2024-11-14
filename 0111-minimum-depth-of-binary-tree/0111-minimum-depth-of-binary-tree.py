# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive approach
        if root is None:
            return 0
        
        if root.left is not None and root.right is not None:
            leftDepth = self.minDepth(root.left)
            rightDepth = self.minDepth(root.right)
            return min(leftDepth, rightDepth) + 1
        elif root.left is None:
            rightDepth = self.minDepth(root.right)
            return rightDepth + 1
        else:
            leftDepth = self.minDepth(root.left)
            return leftDepth + 1

        
#         # Iterative approach
#         if root is None: # base case
#             return 0
        
#         stack = [(root, 1)]
#         min_depth = float('inf')
        
#         while stack != []:
#             node, depth = stack.pop()
            
#             # if leaf node is reached, update answer
#             if node.left == None and node.right == None:
#                 min_depth = min(min_depth, depth)
            
#             if node.left is not None:
#                 stack.append((node.left, depth+1))
#             if node.right is not None:
#                 stack.append((node.right, depth+1))
                
#         return min_depth