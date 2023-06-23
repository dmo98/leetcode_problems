# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using the fast and slow pointer approach, where the fast pointer is "next" and the slow pointer is "prev", and maintaining a HashSet to detect duplicates.
        
        # Edge Cases
        if head is None or head.next is None:
            return head
        prev_pointer = head
        next_pointer = head.next
        
        uniqueNums = set()
        uniqueNums.add(prev_pointer.val)
        
        while next_pointer is not None:
            if next_pointer.val in uniqueNums:
                # delete the node at "next"
                prev_pointer.next = next_pointer.next
                next_pointer = next_pointer.next
            else:
                uniqueNums.add(next_pointer.val)
                prev_pointer = prev_pointer.next
                next_pointer = next_pointer.next
        return head
            
        