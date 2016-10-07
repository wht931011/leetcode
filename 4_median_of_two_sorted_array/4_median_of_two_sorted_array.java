//not efficiency enough
//O(max[m,n])ß
public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int i = 0, j =0;
        List<Integer> result = new ArrayList<Integer>();
        while(i<nums1.length && j<nums2.length){
            if(nums1[i]<=nums2[j]){
                result.add(nums1[i]);
                i++;
            }else{
                result.add(nums2[j]);
                j++;
            }
        }
        if(i==nums1.length){
            for(j=j;j<nums2.length;j++){
                result.add(nums2[j]);
            }
        }
        if(j==nums2.length){
            for(i=i;i<nums1.length;i++){
                result.add(nums1[i]);
            }
        }
        if (result.size() % 2 == 0)
            return ((double)result.get(result.size()/2) + (double)result.get(result.size()/2 - 1))/2;
        else
            return (double) result.get(result.size()/2);
    }
}