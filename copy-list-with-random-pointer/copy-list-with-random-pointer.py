"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy 
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # Create a dictionary that maps each node in 'head' to a Node instance with the same value as the original node
        deepcopy = {None:None}
        node = head
        while node is not None:
            deepcopy[node] = Node(x=node.val)
            node = node.next
        # Mapping the nodes in 'head' to new Node instances (using 'deepcopy') with the same val, next and random fields
        node = head
        output = deepcopy[head]
        output_node = output
        while node is not None:
            output_node.next = deepcopy[node.next]
            output_node.random = deepcopy[node.random]
            # Update 'node' and 'output_node'
            node = node.next
            output_node = output_node.next
        return output
            