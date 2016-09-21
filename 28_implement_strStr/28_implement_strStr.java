public class Solution {
    public int strStr(String haystack, String needle) {
        if(needle.length() == 0){
            return 0;
        }
        if(needle == null || haystack == null || needle.length()>haystack.length()){
            return -1;
        }
        for(int i = 0; i<haystack.length();i++){
            if((i+needle.length())>haystack.length()){
                return -1;
            }else{
                //string.substring(0,0)is not first char in string. (0,1) is.
                if(haystack.substring(i,i+needle.length()).equals(needle)){
                    return i;
                }
            }
        }
        return -1;
    }
}