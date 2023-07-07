class Solution {
    public boolean isPalindrome(int x) {
        int y = x;
        int reversedX = 0;
        while(y!=0){
            int lastDigit = y%10;
            reversedX = reversedX*10 + lastDigit;
            y/=10;
        }
        return reversedX == x && x >= 0;
    }
}