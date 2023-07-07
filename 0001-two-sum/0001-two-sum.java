class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        int[] copy = new int[nums.length];
        int temp1 = 0, temp2 = 0;
        for(int i=0; i<nums.length; i++){
            copy[i] = nums[i];
        }
        Arrays.sort(copy);
        int l = 0, r = nums.length - 1;
        while(l < r){
            if(copy[l] + copy[r] == target){
                temp1 = copy[l];
                temp2 = copy[r];
                break;
            } else if(copy[l] + copy[r] < target){
                l++;
            } else {
                r--;
            }
        }
        int k = 0;
        for(int i=0; i<nums.length; i++){
            if(nums[i] == temp1 || nums[i] == temp2){
                ans[k++] = i;
            }
        }
        return ans;
    }
}
/*
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] == target - nums[i]) {
                    return new int[] { i, j };
                }
            }
        }
        // In case there is no solution, we'll just return null
        return null;
    }
}
*/