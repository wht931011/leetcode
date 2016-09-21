public class Solution {
    public boolean isPalindrome(String s) {
        if(s.length() == 0){
            return true;
        }    
        int i = 0;
        int j = s.length()-1;
        s = s.toLowerCase();
        while (i<j){
            if(!Character.isLetterOrDigit(s.charAt(i))){
                i++;
            
            }else if(!Character.isLetterOrDigit(s.charAt(j))){
                j--;
                
            }else if(Character.isLetterOrDigit(s.charAt(i)) && Character.isLetterOrDigit(s.charAt(j))){
    
                if(s.charAt(i) == s.charAt(j)){
                    i++;
                    j--;
                }else{
                    return false;
                }
            }
        }
        return true;
    }
}