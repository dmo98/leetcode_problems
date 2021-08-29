# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Edge Case
        if head is None or head.next is None:
            return None
        """Floyds Cycle Detection Algorithm aka Turtle and Hair"""
        # Initialize the fast and slow pointers
        fast_pointer = head
        slow_pointer = head
        cycle_found = False
        # At each iteration, move the fast pointer by 2 steps, the slow pointer by 1 step. If they match, we have a cycle. But if the loop breaks without any matching, then the end of the linked list was reached.
        while fast_pointer is not None and fast_pointer.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            if fast_pointer is slow_pointer:
                cycle_found = True
                break
        # If the end of the linked list was reached, we don't have a cycle. Return None
        if not cycle_found:
            return None
        # Reset the slow pointer to head. Keep moving the slow and fast pointers by 1 step at each iteration until they match. The node at which they match is the node where the cycle begins
        slow_pointer = head
        while slow_pointer is not fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        return slow_pointer
        