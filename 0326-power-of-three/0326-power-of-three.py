class Solution {
    public boolean isPowerOfThree(int n) {
        double temp = Math.log10(n)/Math.log10(3);
        return temp == (int) temp;
    }
}