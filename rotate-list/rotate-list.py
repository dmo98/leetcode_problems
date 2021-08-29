# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Edge Case: If 'head' is a linked list with 0 or 1 node, return 'head'
        if head is None or head.next is None:
            return head
        # Accumulate a list containing the values stored in the nodes of the linked list
        nodes = []
        node = head
        while node is not None:
            nodes.append(node.val)
            node = node.next
        # Using the modulus operation to get the effective number of rotations/shifts needed
        shifts = k%len(nodes)
        # Using slicing to rotate 'shifts' elements to the right
        nodes = nodes[-shifts:] + nodes[:-shifts]
        # Creating the rotated linked list. At each step, we get the value from 'nodes' and create a new Node instance
        output = ListNode(val=nodes[0])
        node = output
        index = 1
        while index < len(nodes):
            node.next = ListNode(val=nodes[index])
            node = node.next
            index += 1
        # Append None to the tail of the rotated linked list
        node.next = None
        return output
        
        