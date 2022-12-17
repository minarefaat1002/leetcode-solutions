class Solution {
public:
    int divide(int dividend, int divisor) {
      
       if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }
        int a=dividend/divisor;
        int result = trunc(a);
        return result;   
       
    }
};