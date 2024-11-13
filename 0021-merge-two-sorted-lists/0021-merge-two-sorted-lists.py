# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases: empty linked lists
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1

        # Two Pointers
        start = True

        while (list1 is not None) and (list2 is not None):
            if list1.val <= list2.val:
                if start:
                    head = list1
                    curr = head
                    start = False
                else:
                    curr.next = list1
                    curr = curr.next
                
                list1 = list1.next
            else:
                if start:
                    head = list2
                    curr = head
                    start = False
                else:
                    curr.next = list2
                    curr = curr.next

                list2 = list2.next

        # attaching the tails if either one isn't exhausted
        if list1 is not None:
            curr.next = list1
        
        if list2 is not None:
            curr.next = list2
        
        return head
        