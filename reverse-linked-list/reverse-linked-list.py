# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Edge Case: If head is a linked list with 0 or 1 element, then return head
        if head is None or head.next is None:
            return head
        previous_node = head # will be used to remove 'current_node' from the linked list
        current_node = head.next # will be added to the head after removal from the linked list
        current_head = head # the node to which 'current_node' will be added
        while current_node is not None:
            # remove 'current_node' from the linked list
            new_head = current_node
            next_node = current_node.next
            previous_node.next = next_node
            # add 'current_node' to 'current_head' so that it is now at the head
            new_head.next = current_head
            # update 'current_head' and 'current_node'
            current_head = new_head
            current_node = next_node
            #previous_node = previous_node.next
        return current_head
        
            
        