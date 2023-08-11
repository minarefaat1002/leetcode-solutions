/**
 * @param {number[]} nums
 * @return {number}
 */
var reverseNumber = function (num){
    let reversedNumber = 0;
    while(num!=0){
        reversedNumber = reversedNumber * 10 + num%10;
        num = parseInt(num/10);
    }
    return reversedNumber;
}
var countNicePairs = function(nums) {
    var total = 0;
    const MOD = Math.pow(10,9) + 7;
    let map = new Map();
    for(let num of nums){
        a = num - reverseNumber(num);
        map.set(a,(map.get(a) || 0 ) + 1)
    }
    for(let [key,value] of map){
        total = (total + value*(value-1)/2)%MOD;
    }
    return total    
};