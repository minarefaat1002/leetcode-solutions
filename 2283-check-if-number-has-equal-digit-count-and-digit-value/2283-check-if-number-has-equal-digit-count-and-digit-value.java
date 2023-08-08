class Solution {
    public boolean digitCount(String num) {
        int[] count = new int[10];
        Arrays.fill(count,0);
        for(int i=0;i<num.length();i++){
            count[num.charAt(i)-'0']++;
        }
        for(int i=0;i<num.length();i++){
            if (num.charAt(i)-'0' != count[i]) return false;
        }
        return true;
    }
}