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

import java.lang.Math;

class Solution {
    public int getDecimalValue(ListNode head) {
        ArrayList<Integer> digits = new ArrayList<Integer>();
        ListNode currentNode = head;
        while (currentNode != null){
            digits.add(currentNode.val);
            currentNode = currentNode.next;
        }
        int value = 0;
        for (int i = 0; i < digits.size(); i++){
            if (digits.get(i) == 1){
                value += Math.pow(2, digits.size() - i - 1);
            }
        }
        return value;
            
    }
}