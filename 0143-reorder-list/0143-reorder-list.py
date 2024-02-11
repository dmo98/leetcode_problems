# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the midpoint
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        # reverse the second half    
        curr = slow.next
        slow.next = None
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # merge the two halves
        first = head
        second = prev
        while second is not None:
            next_node = first.next
            next_node_rev = second.next
            first.next = second
            first.next.next = next_node
            first = next_node
            second = next_node_rev