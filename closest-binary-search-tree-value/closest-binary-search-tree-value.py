from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # trivial approach: traverse BST using BFS, keep track of the closest value so far
        
        queue = deque([root])
        closest = (float("inf"), float("inf"))
        
        while len(queue) != 0:
            node = queue.popleft()
            diff = abs(node.val - target)
            if diff <= closest[1]:
                if diff == closest[1]:
                    if node.val < closest[0]:
                        closest = node.val, diff
                else:
                    closest = node.val, diff 
            
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
                
        return closest[0]
            
        
