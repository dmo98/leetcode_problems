/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode currentNode = head;
        int size = 0;
        while (currentNode != null){
            size += 1;
            currentNode = currentNode.next;
        }
        
        int middleIndex;
        if (size%2 == 0){
            middleIndex = size/2;
        }
        else {
            middleIndex = (size-1)/2;
        }
        
        currentNode = head;
        int currentIndex = 0;
        while (currentIndex < middleIndex){
            currentIndex += 1;
            currentNode = currentNode.next;
        }
        return currentNode;
    }
}