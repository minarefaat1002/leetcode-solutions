class Solution {
public:
    // int sum_of_squares(int num){
    //     int sum=0;
    //     while(num){
    //         int digit=num%10;
    //         sum+=digit*digit;
    //         num/=10;
    //     }
    //     return sum;
    // }
    // bool isHappy(int n) {
    //     unordered_set<int> visited;
    //     while(visited.find(n)==visited.end()){ // if it reaches the end . that means n isn't in the visited numbers .
    //         visited.insert(n);
    //         n=sum_of_squares(n);
    //         if(n==1)
    //             return true;
    //     }
    //     return false;
    // }
    int sum_of_squares(int num){
        int sum=0;
        while(num){
            int digit=num%10;
            sum+=digit*digit;
            num/=10;
        }
        return sum;
    }
    bool isHappy(int n) {
        int slow_sum = n;
        int fast_sum = sum_of_squares(n);
        if(slow_sum==1 || fast_sum==1)
            return true;
        while(slow_sum!=fast_sum){
            slow_sum=sum_of_squares(slow_sum);
            fast_sum=sum_of_squares(sum_of_squares(fast_sum));
            if(slow_sum==1 || fast_sum==1)
                return true;
        }
        return false;

    }
};