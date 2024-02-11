# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Two Pointers
        p1 = list1
        p2 = list2
        
        answer = ListNode(val=0, next=None) # dummy node, will be removed at the end
        curr = answer
        while p1 is not None and p2 is not None: # terminates when one of the SLL is exhausted
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        
        # empty out one of the SLL (if other is exhausted before)
        if p1 is not None:
            curr.next = p1
        if p2 is not None:
            curr.next = p2

        return answer.next