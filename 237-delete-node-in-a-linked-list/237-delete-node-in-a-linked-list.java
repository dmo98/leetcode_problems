/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        // Incorrect Approach, left shift all nodes to the right of the given node,           //get rid of last node
        
        // After glance at solution
        node.val = node.next.val;
        node.next = node.next.next;
        
    }
}