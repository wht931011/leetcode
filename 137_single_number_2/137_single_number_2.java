//O(n) but need extra space
public class Solution{
    public int singleNumber(int[] nums) {
        HashMap<Integer,Integer> re = new HashMap<>();
        for(int num : nums){
            if(re.containsKey(num)){
                re.put(num,re.get(num)+1);
            }else{
                re.put(num,1);
            }
        }
        for(int key : re.keySet()){
            if(re.get(key)==1){
                return key;
            }
        }
        return 0;
    }
}