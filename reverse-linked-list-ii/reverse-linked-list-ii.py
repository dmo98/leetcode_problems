# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None or left == right:
            return head
        curr = head
        position = 1
        while position < left:
            prev = curr
            curr = curr.next
            position += 1
        left_node = curr
        
        prev_node = None
        while position <= right:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
            
            position += 1
        right_node = prev_node
        rest = curr
        
        if left != 1:
            prev.next = right_node
        else:
            head = right_node
        left_node.next = rest
        return head
        