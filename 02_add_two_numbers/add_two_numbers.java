/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        //create a head
        ListNode re = new ListNode(0);
        ListNode tmp1 = l1,tmp2 = l2, tmp0 = re;
        while(tmp1 != null || tmp2 != null){
            int x = 0, y=0;
            if(tmp1 != null){
                x = tmp1.val;
                tmp1 = tmp1.next;
            }
            if(tmp2 != null){
                y = tmp2.val;
                tmp2 = tmp2.next;
            }
            int value = x + y + carry;
            carry = value/10;
            value = value%10;

            tmp0.next = new ListNode(value);
            tmp0 = tmp0.next;
        }

        //input like [5] [5], should have 1 more node for the carry at the end.
        if(carry>0){
            tmp0.next = new ListNode(carry);
        }
        return re.next;
    }
    
}