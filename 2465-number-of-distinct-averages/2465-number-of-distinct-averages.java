class Solution {
    public int distinctAverages(int[] nums) {
        HashSet<Double> set = new HashSet<Double>();
        Arrays.sort(nums);
        int l = 0;
        int r = nums.length - 1;
        while(l <= r){
            double avg = (nums[l] + nums[r])/2.0;
            set.add(avg);
            l++;
            r--;
        }
        return set.size();
    }
}