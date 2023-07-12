from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # Recursively traverse the BST, keeping track of the closest value so far. Stop when you hit a leaf in the appropriate branch.
        def closestValueHelper(node, target, closestSoFar):
            if node is None:
                return closestSoFar
            
            if target < node.val:
                # print('left')
                # traverse left sub-tree and update closest so far
                if abs(node.val - target) <= abs(closestSoFar - target):
                    if abs(node.val - target) == abs(closestSoFar - target):
                        closestSoFar = min(closestSoFar, node.val)
                    else:
                        closestSoFar = node.val
                    
                return closestValueHelper(node.left, target, closestSoFar)
                
            else:
                # print('right')
                # traverse right sub-tree and update closest so far
                if abs(node.val - target) <= abs(closestSoFar - target):
                    if abs(node.val - target) == abs(closestSoFar - target):
                        closestSoFar = min(closestSoFar, node.val)
                    else:
                        closestSoFar = node.val
                        
                return closestValueHelper(node.right, target, closestSoFar)
                
        return closestValueHelper(root, target, root.val)
                        
            
        
        
#         # trivial approach: traverse BST using BFS, keep track of the closest value so far
        
#         queue = deque([root])
#         closest = (float("inf"), float("inf"))
        
#         while len(queue) != 0:
#             node = queue.popleft()
#             diff = abs(node.val - target)
#             if diff <= closest[1]:
#                 if diff == closest[1]:
#                     if node.val < closest[0]:
#                         closest = node.val, diff
#                 else:
#                     closest = node.val, diff 
            
#             if node.left is not None:
#                 queue.append(node.left)
#             if node.right is not None:
#                 queue.append(node.right)
                
#         return closest[0]
            
        
