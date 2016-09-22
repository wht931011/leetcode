public class Solution {
    public boolean isNumber(String s) {
        int i = 0, len = s.length();
        boolean has_plus_minus = false;
        boolean has_dot = false;
        boolean has_Num = false;
        boolean has_E = false;
        //get rid of leading whitespace
        while(i<len && Character.isWhitespace(s.charAt(i))){
            i++;
        }
        //check whether the has have positive or minus signal
        if(i<len && s.charAt(i) == '+'){
            i++;
        }else if(i< len &&s.charAt(i)=='-'){
            i++;
        }
        while(i<len && !Character.isWhitespace(s.charAt(i))){
            if(!Character.isDigit(s.charAt(i))){
                //check dot. No e and dot before.
                if(s.charAt(i) == '.'&&!has_E&&!has_dot){
                    has_dot = true;
                    i++;
                //check e. No e before and must have number before
                }else if (s.charAt(i) == 'e'&&!has_E && has_Num){
                        has_E = true;
                        i++;
                //after e, there can be '+' or '-' but '+' or '-' can't appear before
                }else if(has_E && (s.charAt(i) == '+'||s.charAt(i) == '-') && !has_plus_minus){
                        has_plus_minus = true;
                        i++;
                }else{
                    return false;
                }
            }else{
                has_Num = true;
                i++;
            }
        }
        // 1)'-','+','e' can't be the last one. 2)If only ".",return false
        if(s.charAt(i-1)=='-' || s.charAt(i-1) == '+' ||s.charAt(i-1) == 'e' || !has_Num){
            return false;
        }
        //check the tailing whiespace
        while(i<len){
            if(Character.isWhitespace(s.charAt(i))){
                i++;
            }else{
                return false;
            }
        }
        return true;
    }
}