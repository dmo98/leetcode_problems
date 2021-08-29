# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current_node = head
        number_of_nodes = 0
        while current_node is not None:
            number_of_nodes += 1
            current_node = current_node.next
        if n == number_of_nodes:
            new_head = head.next
            return new_head
        else:
            #head_node = head
            current_node = head
            position = number_of_nodes - n
            while position > 0:
                previous_node = current_node
                current_node = current_node.next
                position -= 1
            next_node = current_node.next
            previous_node.next = next_node
            return head
            
        