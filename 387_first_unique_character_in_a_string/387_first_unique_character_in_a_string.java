public class Solution {
    public int firstUniqChar(String s) {
        if(s=="" || s == null){
            return -1;
        }
        HashMap<Character,Integer> re = new HashMap<Character,Integer>();
        char[] s1 = s.toCharArray();
        for(int i=0;i<s1.length;i++){
            if(!re.containsKey(s1[i])){
                re.put(s1[i],i);
            }else{
                re.put(s1[i],-1);
            }
        }
        for(char c : s1){
            if(re.get(c)!=-1){
                return re.get(c);
            }
        }
        return -1;
    }
}