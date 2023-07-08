class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int l = 1, r = nums.length, result = Integer.MAX_VALUE, mid, windowSum;
        boolean found;
        while( l <= r ){
            mid = (l+r)/2;
            windowSum = 0;
            found = false;
            for( int i = 0; i < mid; i++){
                windowSum += nums[i];
            }
            if(windowSum >= target){
                found = true;
            }
            for( int i = mid; i < nums.length; i++ ){
                windowSum += nums[i] - nums[i-mid];
                if( windowSum >= target){
                    found = true;
                    r = mid - 1;
                    break;
                }
            }
            if(found){
                result = Math.min(result,mid);
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return result != Integer.MAX_VALUE? result : 0;
    }
}

// class Solution {
//     public int minSubArrayLen(int target, int[] nums) {
//         int l = 0;
//         int curSum = 0;
//         int result = Integer.MAX_VALUE;
//         for(int r = 0; r < nums.length; r++){
//             curSum += nums[r];
//             while(curSum >= target){
//                 result = Math.min(result,r-l+1);
//                 curSum-=nums[l];
//                 l+=1;
//             }
//         }
//         return result != Integer.MAX_VALUE? result : 0;
//     }
// }