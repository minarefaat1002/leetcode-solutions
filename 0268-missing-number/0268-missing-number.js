/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
//     nums.sort(function(a,b){return a-b});
//     for(let index in nums){
//         if(index!=nums[index]) return index;
//     }
//     return nums.length
    let n = nums.length;
    let sum = n*(n+1)/2;
    for(let num of nums) sum-=num;
    return sum
    
    
    
    
//             Arrays.sort(nums);
//         for(int i = 0; i<nums.length;i++){
//             if(i!=nums[i]) return i;
//         }
//         return nums.length;

        
//         int n = nums.length;
//         int sum = n*(n+1)/2;
//         for(int num : nums){
//             sum-=num;
//         }
//         return sum;
};