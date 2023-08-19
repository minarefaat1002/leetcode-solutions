/**
 * @param {number[]} nums
 * @return {number}
 */
var distinctAverages = function(nums) {
        let set = new Set();
        nums.sort((a,b)=>{return a - b});
        let l = 0;
        let r = nums.length - 1;
        while(l <= r){
            let avg = (nums[l] + nums[r])/2;
            set.add(avg);
            l++;
            r--;
        }
        return set.size;
};