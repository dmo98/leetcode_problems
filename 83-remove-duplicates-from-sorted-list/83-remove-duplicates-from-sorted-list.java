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
    public ListNode deleteDuplicates(ListNode head) {
        // Edge Case 1: LinkedList is empty
        if (head == null) {
            return null;
        }
        ArrayList<Integer> uniqueNums = new ArrayList<Integer>();
        ListNode currentNode = head;
        
        uniqueNums.add(currentNode.val);
        currentNode = currentNode.next;
        
        while (currentNode != null){
            if (currentNode.val != uniqueNums.get(uniqueNums.size()-1)){
                uniqueNums.add(currentNode.val);
            }
            currentNode = currentNode.next;
        }
        
        ListNode output = new ListNode(uniqueNums.get(0));
        currentNode = output;
        for (int i = 1; i < uniqueNums.size(); i++){
            currentNode.next = new ListNode(uniqueNums.get(i));
            currentNode = currentNode.next;
        }
        currentNode.next = null;
        
        return output;
    }
}