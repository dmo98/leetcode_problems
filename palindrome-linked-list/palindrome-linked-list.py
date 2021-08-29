# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node_values = []
        current_node = head
        while current_node is not None:
            node_values.append(current_node.val)
            current_node = current_node.next
        
        for index in range(0, len(node_values)//2):
            if node_values[index] != node_values[len(node_values)-1-index]:
                return False
        return True
        