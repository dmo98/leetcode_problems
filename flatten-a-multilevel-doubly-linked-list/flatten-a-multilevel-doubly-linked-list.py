"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
import copy
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # Edge Case: If the linked list is empty, return it
        if head is None:
            return None

        output = head   # Initialize the output linked list
        output.prev = None
        node = output
        nodes = []      # All the nodes that have children get appended to this list for later
        
        while True:
            # When you have reached the end of the entire multilevel linked list, break out of the loop
            if len(nodes) == 0 and node.next is None and node.child is None:
                break
            # When you have reached the end of the linked list on 1 level, continue where the parent linked list left off
            elif node.next is None and node.child is None and len(nodes) >= 1:
                # In case multiple parent linked lists had children at their last node. (E.g. a vertical structure)
                while nodes[-1].next is None:
                    nodes.pop()
                    if len(nodes) == 0:
                        break
                if len(nodes) == 0:
                    break
                # If you can still continue where the parent linked list left off
                node.next = nodes[-1].next
                node.next.prev = node
                node = node.next
                nodes.pop()
            elif node.child is not None:
                # If a node has a child, go down that route. Append the node to 'nodes' for continuation later on
                nodes.append(copy.deepcopy(node))
                node.next = node.child
                node.child = None
                node.next.prev = node
                node = node.next
            elif node.child is None and node.next is not None:
                # For regular horizontal traversal
                node.next.prev = node
                node = node.next
            
        # Append None to the tail
        node.next = None
        return output