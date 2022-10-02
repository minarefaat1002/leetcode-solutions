class Solution {
public:
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
        unordered_set<int> visited;
        while(visited.find(n)==visited.end()){ // if it reaches the end . that means n isn't in the visited numbers .
            visited.insert(n);
            n=sum_of_squares(n);
            if(n==1)
                return true;
        }
        return false;
    }
};