class Solution {
    public int semiOrderedPermutation(int[] nums) {
        int minIndex = -1;
        int maxIndex = -1;
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for(int i = 0;i<nums.length;i++){
            if(nums[i] < min){
                min = nums[i];
                minIndex = i;
            }
            if(nums[i] > max){
                max = nums[i];
                maxIndex = i;
            }
        }
        int totalSwaps = minIndex + (nums.length - maxIndex - 1);
        return maxIndex > minIndex ? totalSwaps : totalSwaps - 1;
    }
}