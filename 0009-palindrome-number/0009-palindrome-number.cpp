class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0){
            return false;
        }
        long long reverse = 0;
        int temp = x;
        while(temp){
            int digit = temp%10;
            temp = temp/10;
            reverse = reverse*10 + digit;
        }
        if(x==reverse){
            return true;
        } else {
            return false;
        }
    }
};