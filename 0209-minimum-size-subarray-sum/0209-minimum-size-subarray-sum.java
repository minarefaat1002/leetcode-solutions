class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int l = 0;
        int curSum = 0;
        int result = Integer.MAX_VALUE;
        for(int r = 0; r < nums.length; r++){
            curSum += nums[r];
            while(curSum >= target){
                result = Math.min(result,r-l+1);
                curSum-=nums[l];
                l+=1;
            }
        }
        return result != Integer.MAX_VALUE? result : 0;
    }
}