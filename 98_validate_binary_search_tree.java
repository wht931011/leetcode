/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

//first do binary tree inorder travasl and store it in a arraylist
//then check whether it is increasing
public class Solution {
    public boolean isValidBST(TreeNode root) {
        List<Integer> re = new ArrayList<>();
        inOrder(root,re);
        if(re.size() == 1){
            return true;
        }
        int previous = Integer.MIN_VALUE;
        for(int n = 0; n<re.size();n++){
            if(n+1!=re.size()){
                if(re.get(n) >= re.get(n+1)){
                    return false;
                }
            }
        }
        return true;
    }
    
    void inOrder(TreeNode root, List re){
        if(root != null){
            inOrder(root.left,re);
            re.add(root.val);
            inOrder(root.right,re);
        }
    }
}