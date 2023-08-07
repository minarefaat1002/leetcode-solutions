/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    for(let i = 0;i<Math.trunc(s.length/2);i++){ // Math.trunc ==> removes the decimal part .
        let temp = s[i];
        s[i] = s[s.length-i-1];
        s[s.length-i-1] = temp;
    }
};