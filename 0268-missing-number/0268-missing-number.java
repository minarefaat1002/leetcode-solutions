class Solution {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        for(int i = 0; i<nums.length;i++){
            if(i!=nums[i]) return i;
        }
        return nums.length;

        
//         int n = nums.length;
//         int sum = n*(n+1)/2;
//         for(int num : nums){
//             sum-=num;
//         }
//         return sum;
    }
}