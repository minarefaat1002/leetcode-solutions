class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int l = 1;
        int r = nums.length;
        int result = Integer.MAX_VALUE;
        while( l <= r ){
            int mid = (l+r)/2;
            int windowSum = 0;
            boolean found = false;
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