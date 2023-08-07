/**
 * @param {number[]} nums
 * @return {number}
 */
var mostFrequentEven = function(nums) {
    let map = {};
    let mostRepetitions = 0;
    let mostRepeated = -1;
    for(num of nums){
        if(num%2===0){
            if(!map[num]) map[num] = 0;
            map[num]++;
        }
    }
    for(let key in map){
        key = Math.trunc(key); // cause key is string in the (for...in) loop
        if (map[key] > mostRepetitions){
            mostRepetitions = map[key];
            mostRepeated = key;
        } else if(map[key]===mostRepetitions && key < mostRepeated){
            mostRepeated = key;
        }
    }
    return mostRepeated;
};