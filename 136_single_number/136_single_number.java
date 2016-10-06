//O(n) but need extra space 
public class Solution_1{
    public int singleNumber(int[] nums) {
        HashMap<Integer,Integer> re = new HashMap<>();
        for(int num : nums){
            if(re.containsKey(num)){
                re.put(num,num);
            }else{
                re.put(num,null);
            }
        }
        for(int key : re.keySet()){
            if(re.get(key)==null){
                return key;
            }
        }
        return 0;
    }
}
//O(n) and also no extra space. Logic: Xor (x^x = 0, x^0 = x, 1^1^0 = 0 = 1^0^1)
public class Solution {
    public int singleNumber(int[] nums) {
        int num = 0;
        for (int x : nums) {
            num ^= x;
        }
        return num;
    }
}

