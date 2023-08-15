class Solution {
    public int sumFourDivisors(int[] nums) {
        int total = 0;
        for(Integer num:nums){
            int sq = (int)(Math.sqrt(num));
            int divisors = 0;
            int Sum = 0;
            for(int i = 1; i<sq+1;i++){
                if(num%i == 0){
                    divisors += (num/i != sq) ? 2 : 1;
                    Sum += i + num/i;
                }
            }
            if(divisors == 4){
                total += Sum;
            }
        }
        return total;
    }
}