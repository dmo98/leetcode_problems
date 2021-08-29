# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Edge Cases: If both linked lists are empty, return None. If either one is empty, return the other
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        # Obtaining the first node (head) of the merged linked list. 
        if l1.val <= l2.val:
            merged_list_head = ListNode(val=l1.val)
            merged_list = merged_list_head
            l1 = l1.next
        elif l1.val > l2.val:
            merged_list_head = ListNode(val=l2.val)
            merged_list = merged_list_head            
            l2 = l2.next
        # Obtaining the other nodes of the merged linked list, as long as l1 and l2 aren't empty.
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                merged_list.next = ListNode(val=l1.val)
                merged_list = merged_list.next
                l1 = l1.next
            elif l1.val > l2.val:
                merged_list.next = ListNode(val=l2.val)
                merged_list = merged_list.next
                l2 = l2.next
        # If either linked list is empty and the other still has nodes, append the nodes of the other to the merged linked list
        if l1 is None and l2 is not None:
            merged_list.next = l2
        elif l2 is None and l1 is not None:
            merged_list.next = l1
        # Return the head of the merged linked list
        return merged_list_head
            
        