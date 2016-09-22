public class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int base = 1;
        int temp = x;
        //if not divide by 10, base will have one more zero.
        temp /=10;
        while(temp>0){
            temp /=10;
            base *=10;
        }
        while(x>0){
            //compare first digit and the last digit
            if((x/base) != (x%10)){
                return false;
            }
            //remove the first digit
            x %= base;
            //remove the last digit
            x /= 10;
            //2 digits have been removed
            base /=100;
        }
        return true;
    }
}