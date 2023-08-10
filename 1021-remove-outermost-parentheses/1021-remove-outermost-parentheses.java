class Solution {
    public String removeOuterParentheses(String s) {
        String newS = "";
        int leftParenthesis = 0;
        for(int i = 0; i<s.length();i++){
            char c = s.charAt(i);
            if(c == '(' && leftParenthesis == 0) {
                leftParenthesis += 1;
            } else if(c == '(' && leftParenthesis >= 1) {
                newS += c;
                leftParenthesis += 1;
            } else if(c==')' && leftParenthesis == 1){
                leftParenthesis = 0;
            } else {
                newS += c;
                leftParenthesis -= 1;
            }
        }
        return newS;
    }
}