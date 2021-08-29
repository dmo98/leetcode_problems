# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Edge Case: If 'head' is an empty linked list, return None
        if head is None:
            return None
        index = 0 # needed if the element to be removed is at the head of the linked list
        previous_node = None # needed to remove an element that isn't at the head
        current_node = head
        while current_node is not None:
            # If you find a node that needs to be removed
            if current_node.val == val:
                # If 'current_node' is at the head of the linked list, assign the next node as the head of the linked list and remove the current node
                if index == 0:
                    new_head = current_node.next
                    head = new_head
                    current_node = head
                    continue
                # If 'current_node' isn't at the head of the linked list, remove the current node
                else:
                    next_node = current_node.next
                    previous_node.next = next_node
                    current_node = next_node
                    continue
            # If you don't find a node that needs to be removed, update 'previous_node' and 'current_node'. Increment 'index' so that we know we're no longer at the head of the linked list.      
            index += 1
            previous_node = current_node
            current_node = current_node.next
        return head
        