//O(n)
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer>map = new HashMap<>();
        for(int m =0;m<nums.length;m++){
            if(map.containsKey(target - nums[m])){
                return new int[] {m,map.get(target-nums[m])};
            }else{
                map.put(nums[m],m);
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
