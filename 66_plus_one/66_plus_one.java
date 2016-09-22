public class Solution {
    public int[] plusOne(int[] digits) {
        int carry = 0;
        for(int i = digits.length-1; i>=0;i--){
            if(digits[i]<9){
                digits[i] = digits[i] + 1;
                carry = 0;
                break;
            }else{
                digits[i] = 0;
                carry = 1;
            }
        }
        if(carry == 0){
            return digits;
        }else{
            int[] re = new int[digits.length+1];
            re[0] = 1;
            for(int n = 1; n< re.length;n++){
                re[n] = digits[n-1];
            }
            return re;
        }
    }
}