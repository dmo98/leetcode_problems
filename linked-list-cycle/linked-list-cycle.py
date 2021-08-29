# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Edge Case
        if head is None or head.next is None: 
            return False
        # Initialize both fast and slow pointers
        fast_pointer = head
        slow_pointer = head
        # Keep moving the fast pointer by 2 steps, slow pointer by 1 step each time until they match. If they match, then it's confirmed that we have a cycle. If the loop breaks, the end of the linked list was reached, so we don't have a cycle
        while fast_pointer is not None and fast_pointer.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            if fast_pointer is slow_pointer:
                return True
        return False