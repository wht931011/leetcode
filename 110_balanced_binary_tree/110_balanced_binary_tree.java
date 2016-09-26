/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
//tutorial video:https://www.youtube.com/watch?v=nOcFiGl5Vy4
public class Solution {
    public boolean isBalanced(TreeNode root) {
        if(getHeight(root)==-1) return false;
        return true;
    }
    
    public int getHeight(TreeNode root){
        if(root == null) return 0;
        int left_sub = getHeight(root.left);
        int right_sub = getHeight(root.right);
        if(left_sub==-1 || right_sub==-1){
            return -1;
        }
        if(Math.abs(left_sub-right_sub) >1) return -1;
        return Math.max(left_sub,right_sub)+1;
    }
}