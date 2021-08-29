# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Traverse the linked lists 'l1' and 'l2', concatenating the values stored in each node to their respective strings
        number1 = ''
        number2 = ''
        node1 = l1
        node2 = l2
        while node1 is not None and node2 is not None:
            number1 += str(node1.val)
            node1 = node1.next
            
            number2 += str(node2.val)
            node2 = node2.next
        # If the two linked lists are of unequal length, one of them will still have nodes. Concatenate the values stored in those nodes to the respective string
        if node1 is None and node2 is not None:
            while node2 is not None:
                number2 += str(node2.val)
                node2 = node2.next
        elif node2 is None and node1 is not None:
            while node1 is not None:
                number1 += str(node1.val)
                node1 = node1.next
        # Get the numbers by reversing the strings and casting them to type int        
        number1 = int(number1[::-1])
        number2 = int(number2[::-1])
        # Get the sum, cast it type string, and reverse that string
        number3 = str(number1 + number2)[::-1]
        
        # Returning the sum as a linked list in reverse order
        output = ListNode(val=int(number3[0])) # the head of the output linked list
        node3 = output
        index = 1
        while index < len(number3):
            node3.next = ListNode(val=int(number3[index]))
            node3 = node3.next
            index += 1
        return output
            
        