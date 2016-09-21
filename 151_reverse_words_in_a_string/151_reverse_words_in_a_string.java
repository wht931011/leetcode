public class Solution {
    public String reverseWords(String s) {
        StringBuilder re = new StringBuilder();
        if(s.length()==0){
            return re.toString();
        }
        String[] split_s = s.split(" ");
        for(int i = split_s.length-1; i >= 0;i--){
            if(!split_s[i].equals("")){
                re.append(split_s[i]+" ");
            }
        }
        if(re.length()!=0){
            return re.substring(0,re.length()-1).toString();
        }else{
            return re.toString();
        }
    }
}