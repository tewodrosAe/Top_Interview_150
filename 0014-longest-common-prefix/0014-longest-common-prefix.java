class Solution {
    public String longestCommonPrefix(String[] strs) {
        int len = strs.length;
        if(len == 0){
            return "";
        }

        String prefix = strs[0];

        for(int i=1; i<len;i++){
            while(strs[i].indexOf(prefix)!=0){
                prefix = prefix.substring(0, prefix.length()-1);
            }
        }
        return prefix;

        
    }
}