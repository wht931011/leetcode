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
    public boolean isSymmetric(TreeNode root) {
        if(root == null){
            return true;
        }
        return isSym_tree(root.left, root.right);
    }
    
    public boolean isSym_tree(TreeNode lr,TreeNode rr){
        if(lr==null && rr==null){
            return true;
        }
        if(lr==null || rr==null){
            return false;
        }
        if(lr.val == rr.val){
            return isSym_tree(lr.left,rr.right) && isSym_tree(lr.right,rr.left);
        }
        return false;
    }
}