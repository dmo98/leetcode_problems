# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
#         # Iterative solution: didn't get it
#         stack = [(root, float('inf'), -float('inf'))]
#         answer = -float('inf')
        
#         while stack != []:
#             node, minVal, maxVal = stack.pop()
#             answer = max(answer, maxVal - minVal)
            
#             if node.left is not None:
#                 stack.append((node.left, min(minVal, node.val), max(maxVal, node.val)))
#             if node.right is not None:
#                 stack.append((node.right, min(minVal, node.val), max(maxVal, node.val)))
                
#         return answer
        
        # Recursive solution
        def dfs(node, minVal, maxVal):
            if node is None:    # base case
                return maxVal - minVal
            
            left = dfs(node.left, min(minVal, node.val), max(maxVal, node.val))
            right = dfs(node.right, min(minVal, node.val), max(maxVal, node.val))
            
            return max(left, right)
        
        return dfs(root, float('inf'), -float('inf'))
        