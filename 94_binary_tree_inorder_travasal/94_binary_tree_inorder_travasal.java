/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

//**important**
//recursive
//algorithm tutorial https://www.youtube.com/watch?v=nzmtCFNae9k
public class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        ArrayList<Integer> result = new ArrayList<Integer>();
        TreeNode curt = root;
        while (curt != null || !stack.empty()) {
            while (curt != null) {  //keep going left until there is no left.
                stack.add(curt);    //add root to the stack
                curt = curt.left;
            }
            curt = stack.peek();    //get first of the stack (kind of back track)
            stack.pop();            //remove the first of stack
            result.add(curt.val);   //add to result
            curt = curt.right;      //check right child.
        }
        return result;
    }
}

//recurisve(easy)
public class Solution2 {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> re = new ArrayList<>();
        inOrder(root,re);
        return re;
    }
    
    void inOrder(TreeNode root, List re){
        if(root != null){
            inOrder(root.left,re);
            re.add(root.val);
            inOrder(root.right,re);
        }
    }
}