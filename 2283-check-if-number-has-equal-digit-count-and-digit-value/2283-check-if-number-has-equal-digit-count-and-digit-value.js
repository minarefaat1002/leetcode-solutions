/**
 * @param {string} num
 * @return {boolean}
 */
var digitCount = function(num) {
        const count = Array(10).fill(0);
        for(let i=0;i<num.length;i++){
            count[num[i]]++;
        }
        for(let i=0;i<num.length;i++){
            if (num[i] != count[i]) return false;
        }
        return true;
};