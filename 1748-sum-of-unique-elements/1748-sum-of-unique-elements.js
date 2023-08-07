/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfUnique = function(nums) {
    const arr = Array(101).fill(0);
    let total = 0;
    for(num of nums)arr[num]++;
    for(let i = 0; i < arr.length;i++){
        if(arr[i]===1) total+=i;
    }
    return total;
};