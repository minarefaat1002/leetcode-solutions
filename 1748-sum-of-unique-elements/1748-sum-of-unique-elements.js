/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfUnique = function(nums) {
  //    let map = {};
  // let sum = 0;
  // for (let num of nums) {
  //   map[num] = map[num] + 1 || 1;
  // }
  // for (let key in map) {
  //   if (map[key] === 1) {
  //     sum += +key;
  //   }
  // }
  // return sum;
    const arr = Array(101).fill(0);
    let total = 0;
    for(num of nums)arr[num]++;
    for(let i = 0; i < arr.length;i++){
        if(arr[i]===1) total+=i;
    }
    return total;
};