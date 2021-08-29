# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Edge Cases: If the linked list has 0, 1 or 2 nodes in it, return it
        if head is None or head.next is None or head.next.next is None:
            return head
        
        odd_node = head # 'odd_node' is initialized to the head of the linked list
        even_head = head.next # 'even_head' is the head of the linked list containing nodes at an even index
        even_node = even_head # 'even_node' is initialized to the node at index 1 of the linked list 'head'
        
        while odd_node.next.next is not None and even_node.next.next is not None:
            # Skip the node at the even index. Add the next node at an odd index to the linked list 'head'
            odd_node_ahead = odd_node.next.next
            odd_node.next = odd_node_ahead
            odd_node = odd_node.next    # Update 'odd_node' 
            # Skip the node at the odd index. Add the next node at an even index to the linked list 'even_head'
            even_node_ahead = even_node.next.next
            even_node.next = even_node_ahead
            even_node = even_node.next      # Update 'even_node'
        # If the original linked list contains an odd number of nodes, there will be one last node at an odd index. Add it to 'head'
        if odd_node.next.next is not None:
            odd_node_ahead = odd_node.next.next
            odd_node.next = odd_node_ahead
            odd_node = odd_node.next
        # Add 'None' to 'even_head'. This is the end of the reordered linked list (after 'even_head' is added to 'head')    
        even_node.next = None
        # Add 'even_head' to 'head'
        odd_node.next = even_head
        return head
        
        
        
        