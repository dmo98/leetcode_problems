from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # run BFS, keep track of the sum of values at each level. After BFS terminates, we'll have the sum of the deepest leaf node values.
        
        queue = deque([root])
        
        while len(queue) != 0:
            num_nodes = len(queue)
            level_sum = 0
            
            for i in range(num_nodes):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return level_sum
                