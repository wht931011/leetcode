/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode re = new ListNode(0);
        ListNode tmp1 = l1, tmp2 = l2, tmp0 = re;
        while(tmp1!=null && tmp2!=null){
            if(tmp1.val<tmp2.val){
                tmp0.next = new ListNode(tmp1.val);
                tmp0 = tmp0.next;
                tmp1 = tmp1.next;
            }else{
                tmp0.next = new ListNode(tmp2.val);
                tmp0 = tmp0.next;
                tmp2 = tmp2.next;
            }
        }
        if(tmp1==null){
            tmp0.next = tmp2;
        }
        if(tmp2==null){
            tmp0.next = tmp1;
        }
        return re.next;
    }
}