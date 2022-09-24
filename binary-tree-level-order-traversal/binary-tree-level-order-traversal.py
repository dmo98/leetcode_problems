# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = [(root, 0)]
        levels = {}
        max_level = 0
        
        while len(queue) != 0:
            node, level = queue.pop(0)
            
            if level not in levels.keys():
                levels[level] = [node.val]
            else:
                levels[level].append(node.val)
                
            if level > max_level:
                max_level = level
                
            if node.left != None:
                queue.append((node.left, level+1))
            if node.right != None:
                queue.append((node.right, level+1))
        
        result = []
        for level in range(max_level+1):
            if level in levels.keys():
                result.append(levels[level])
                
        return result