# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Fast and Slow Pointers
        if head.next is None:
            return None
        
        prev = None # node before slow pointer
        slow = head
        fast = head
        
        i = 0
        while i < n:
            fast = fast.next
            i += 1
            
        while fast is not None:
            fast = fast.next
            prev = slow
            slow = slow.next
            
        # prev pointer is at the node before the one to be deleted
        if prev is None:
            return head.next
        else:
            prev.next = slow.next
            return head
    
#         # Brute-force approach
#         # edge case:
#         if head.next is None:
#             return None
        
#         # find the length of the SLL
#         length = 0
#         curr = head
#         while curr is not None:
#             length += 1
#             curr = curr.next
        
#         if length == n:
#             return head.next
        
#         # iterate upto node at position (length - n) -> node before the one to be deleted
#         position = 1
#         curr = head
#         while curr is not None:
#             if position == length - n:
#                 break
#             curr = curr.next
#             position += 1
            
#         curr.next = curr.next.next
#         return head            
        