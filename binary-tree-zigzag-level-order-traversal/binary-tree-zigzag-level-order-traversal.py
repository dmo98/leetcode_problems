from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # run BFS, store over nodes in each level in forward and reverse order (alternating) in a list, append to answer list at the end of each while loop iteration.
        
        if root is None:
            return []
        
        queue = deque([root])
        answer = []
        level = 0
        
        while len(queue) != 0:
            num_nodes = len(queue)
            nodes = []
                
            for i in range(num_nodes):
                node = queue.popleft()
                nodes.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            
            if level % 2 == 1:
                nodes.reverse()
                
            answer.append(nodes)
            level += 1
            
        return answer