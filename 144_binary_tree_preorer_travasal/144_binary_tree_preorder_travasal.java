/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
//iterative version
//algorithm: https://www.youtube.com/watch?v=elQcrJrfObg
public class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        List<Integer> preorder = new ArrayList<Integer>();
        
        if (root == null) {
            return preorder;
        }
        
        stack.push(root);
        while (!stack.empty()) {
            TreeNode node = stack.pop();
            preorder.add(node.val);
            if (node.right != null) {
                stack.push(node.right);
            }
            //Add node.left last because it is stack and print it first.
            if (node.left != null) {
                stack.push(node.left);
            }
        }
        
        return preorder;
    }
}

//recursive version
public class Solution2 {
    public List<Integer> preorderTraversal(TreeNode root) {
        List re = new ArrayList();
        pre(root,re);
        return re;
    }
    
    void pre(TreeNode node, List re){
        if(node != null){
            re.add(node.val);
            pre(node.left,re);
            pre(node.right,re);
        }
    }
}