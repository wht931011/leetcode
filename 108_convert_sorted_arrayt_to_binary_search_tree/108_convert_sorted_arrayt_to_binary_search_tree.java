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
    public TreeNode sortedArrayToBST(int[] nums) {
        return arrayToBST(nums,0,nums.length-1);
    }
    
    public TreeNode arrayToBST(int[] nums, int start, int end) {
        if(start>end) return null;
        int mid = ( end + start ) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = arrayToBST(nums,start,mid-1);
        root.right = arrayToBST(nums,mid+1,end);
        return root;
    }
}