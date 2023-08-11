class Solution {
    public int countNicePairs(int[] nums) {
        long total = 0;
        int MOD = (int)Math.pow(10,9) + 7;
        HashMap<Integer,Long> map = new HashMap<Integer,Long>();
        for (int i = 0; i < nums.length; i++) map.put(nums[i]-reverseNumber(nums[i]),map.getOrDefault(nums[i]-reverseNumber(nums[i]),(long)0)+1);
        for(Map.Entry<Integer,Long> entry : map.entrySet()){
            total += entry.getValue()*(entry.getValue()-1)/2;
            total = total%MOD;
        }
        return (int)total;
    }
    public int reverseNumber(int num){
        int reversedNumber = 0;
        while(num!=0){
            reversedNumber = reversedNumber * 10 + num % 10;
            num = num/10;
        }
        return reversedNumber;
    }
}