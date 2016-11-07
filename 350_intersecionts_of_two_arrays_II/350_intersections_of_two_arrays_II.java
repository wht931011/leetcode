public class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer,Integer> dict = new HashMap<>();
        for(int num : nums1){
            if(dict.containsKey(num)){
                dict.put(num,dict.get(num)+1);
            }else{
                dict.put(num,1);
            }
        }
        List<Integer> re_list = new ArrayList<>();
        for(int num : nums2){
            if(dict.containsKey(num) && dict.get(num)>0){
                re_list.add(num);
                dict.put(num,dict.get(num)-1);
            }
        }
        int[] re = new int[re_list.size()];
        int index = 0;
        for(int num : re_list){
            re[index] = num;
            index++;
        }
        return re;
    }
}