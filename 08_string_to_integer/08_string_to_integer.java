    public int myAtoi(String str) {
        int i = 0, n = str.length(), re = 0;
        boolean isPositive = true;
        while (i < n && Character.isWhitespace(str.charAt(i))){
            i++;
        }
        if (i < n && str.charAt(i) == '+') {
            i++;
        } else if (i < n && str.charAt(i) == '-') {
            isPositive = false;
            i++;
        }
        while (i < n && Character.isDigit(str.charAt(i))) {
            //Integer.MAX_VALUE = 2147483647 Interger.Minvalue = -2147483648. Check before adding to avoid overflow
            if(re > Integer.MAX_VALUE/10 || re == Integer.MAX_VALUE/10 && Character.getNumericValue(str.charAt(i)) >= 8){
                return isPositive ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            re *=10;
            re +=Character.getNumericValue(str.charAt(i));
            i++;
        }
       return isPositive ? re : -re;
    }
}