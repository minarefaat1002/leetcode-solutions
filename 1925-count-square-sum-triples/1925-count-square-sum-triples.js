/**
 * @param {number} n
 * @return {number}
 */
var countTriples = function(n) {
    let counter = 0;
    for(let i = n; i >= 1; i--){
        for(let j = n; j>= 1;j--){
            let c = Math.sqrt(i*i + j*j);
            if(Number.isInteger(c) && c <= n){
                counter += 1;
            }
        }
    }
    return counter;
};