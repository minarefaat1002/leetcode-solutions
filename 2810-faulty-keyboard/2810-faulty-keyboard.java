class Solution {
    public String finalString(String s) {
        // newString = ""
        // for char in s:
        //     if char == "i":
        //         newString = newString[::-1]
        //     else:
        //         newString += char
        // return newString
        StringBuilder newString = new StringBuilder("");;
        for(int i = 0;i<s.length();i++){
            char c = s.charAt(i);
            if(c=='i') newString.reverse();
            else newString.append(c);
        }
        return newString.toString();
    }
}