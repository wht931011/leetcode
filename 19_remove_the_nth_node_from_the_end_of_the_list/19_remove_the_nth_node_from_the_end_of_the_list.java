/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
//O(n)
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode tmp = new ListNode(0);
        tmp.next = head;
        //two pointer, first goes first until n + 1 (cause tmp.next=head,need to move one more)
        ListNode first = tmp;
        ListNode second  = tmp;
        for(int i =0; i< n+1; i++){
            first = first.next;
        }
        //then two pointers goes together. a gap is kept.
        while(first!=null){
            first = first.next;
            second = second.next;
        }
        second.next = second.next.next;
        return tmp.next;
    }
}