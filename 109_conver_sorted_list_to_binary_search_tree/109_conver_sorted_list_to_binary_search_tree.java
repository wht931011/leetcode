/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        return listToBST(head,null);
    }
    
    public TreeNode listToBST(ListNode head, ListNode tail){
        if(head == tail) return null;
        ListNode fast = head;
        ListNode slow = head;
        while(fast.next!=tail&&fast.next.next!=null&&fast.next!=null&&fast.next.next!=tail){
            slow = slow.next;
            fast = fast.next.next;
        }
        TreeNode root = new TreeNode(slow.val);
        root.left = listToBST(head,slow);
        root.right = listToBST(slow.next,tail);
        return root;
    }
}