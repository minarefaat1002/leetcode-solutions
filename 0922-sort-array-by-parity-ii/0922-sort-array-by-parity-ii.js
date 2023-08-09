/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParityII = function(nums) {
        let evenPointer = 0;
        let oddPointer = 1;
        while(evenPointer < nums.length && oddPointer < nums.length){
            if(nums[evenPointer]%2 == 0) evenPointer+=2;
            else if(nums[oddPointer]%2 == 1) oddPointer+=2;
            else {
                let temp = nums[evenPointer];
                nums[evenPointer] = nums[oddPointer];
                nums[oddPointer] = temp;
            }
        }
        return nums;  
};