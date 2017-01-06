public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        helper(n,k,1,result,new ArrayList<Integer>());
        return result;
    }
    public void helper(int n, int k, int start, List<List<Integer>> result, List<Integer> res){
        if(k==0){
            result.add(new ArrayList<Integer>(res));
            return;
        }
        for(int i = start; i <= n; i++){
            res.add(i);
            helper(n,k-1,i+1,result,res);
            res.remove(res.size()-1);
        }
    }
}