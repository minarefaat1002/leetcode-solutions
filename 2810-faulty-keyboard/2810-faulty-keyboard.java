class Solution {
    public String finalString(String s) {
        StringBuilder newString = new StringBuilder("");;
        for(int i = 0;i<s.length();i++){
            char c = s.charAt(i);
            if(c=='i') newString.reverse();
            else newString.append(c);
        }
        return newString.toString();
    }
}