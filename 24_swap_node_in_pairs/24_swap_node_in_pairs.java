/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode tmp = head;
        ListNode tmp2 = new ListNode(0);
        ListNode tmp3 = new ListNode(0);
        ListNode prev = null;
        while(tmp!=null && tmp.next !=null){
            tmp2 = tmp.next;
            tmp3 = tmp.next.next;
            tmp.next = tmp3;
            tmp2.next = tmp;
            //linked with previous swap
            if(prev != null){
                prev.next = tmp2;
            }
            //check head, update head
            if(tmp == head){
                head = tmp2;
            }
            prev = tmp;
            tmp = tmp3;
        }
        return head;
    }
}