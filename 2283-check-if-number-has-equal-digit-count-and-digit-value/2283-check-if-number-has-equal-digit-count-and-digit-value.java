class Solution {
    public boolean digitCount(String num) {
        int[] count = new int[10];
        Arrays.fill(count,0);
        for(int i=0;i<num.length();i++){
            count[Character.getNumericValue(num.charAt(i))]++;
        }
        for(int i=0;i<num.length();i++){
            if (Character.getNumericValue(num.charAt(i)) != count[i]) return false;
        }
        return true;
    }
}