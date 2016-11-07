public class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet<Integer> num1 = new HashSet<>();
        HashSet<Integer> result = new HashSet<>();
        for(int num : nums1){
            num1.add(num);
        }
        for(int num : nums2){
            if(num1.contains(num)){
                result.add(num);
            }
        }
        int size = result.size();
        int[] re = new int[size];
        int index = 0;
        for(int num: result){
            re[index] = num;
            index++;
        }
        return re;
    }
}