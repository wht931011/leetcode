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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> re = new ArrayList<>();
        LinkedList<TreeNode> helper = new LinkedList();
        if(root ==null){
            return re;
        }else{
            helper.add(root);
        }
        while(helper.size()!=0){
            int len = helper.size(),i=0;
            List<Integer> tmp = new ArrayList();
            while(i<len){
                TreeNode tmp_root = (TreeNode) helper.poll();
                tmp.add(tmp_root.val);
                if(tmp_root.left!=null){
                    helper.add(tmp_root.left);
                }
                if(tmp_root.right!=null){
                    helper.add(tmp_root.right);
                }
                i++;
            }
            re.add(tmp);
        }
        return re;
    }
}