# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseOrder(self, head: ListNode) -> List[ListNode]:
        """
        Returns a list of all the nodes in the linked list in reverse order
        """
        current_node = head
        result = []
        while current_node is not None:
            result.append(current_node)
            current_node = current_node.next
        result.reverse()
        return result
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Edge Case: Empty Linked Lists
        if headA is None or headB is None:
            return None
        # Get the reverse order of the 2 linked lists    
        listA = self.reverseOrder(headA)
        listB = self.reverseOrder(headB)
        # Edge Case: Single Element Linked Lists. If their node is the same, return it. Otherwise return None
        if len(listA) == 1 or len(listB) == 1:
            if listA[0] == listB[0]:
                return listA[0]
            else:
                return None
        # Compare the last elements of the linked lists. If they match, increment 'common_nodes', otherwise return the last node that matched (Return None if there were no common nodes)
        common_nodes = 0
        while len(listA) > 0 and len(listB) > 0:
            lastNodeA = listA.pop(0)
            lastNodeB = listB.pop(0)
            if lastNodeA != lastNodeB:
                if common_nodes == 0:
                    return None
                else:
                    return prev_node
            else:
                common_nodes += 1
                prev_node = lastNodeA
        # Edge Case: Both linked lists match perfectly. You'll end up returning the 1st node in that linked list 
        return lastNodeA