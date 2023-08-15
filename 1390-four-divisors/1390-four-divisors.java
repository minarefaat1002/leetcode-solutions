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
        // total = 0
        // for num in nums:
        //     sq = int(sqrt(num))
        //     divisors = 0
        //     Sum = 0
        //     for i in range(1,sq+1):
        //         if num%i == 0:
        //             divisors += 2 if num/i != sq else 1
        //             Sum += i + num//i
        //     if divisors == 4:
        //         total +=Sum
        // return total 