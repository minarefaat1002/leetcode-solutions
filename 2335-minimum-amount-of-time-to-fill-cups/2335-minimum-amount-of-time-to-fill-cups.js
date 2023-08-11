/**
 * @param {number[]} amount
 * @return {number}
 */
var fillCups = function(amount) {
        let seconds = 0;
        amount.sort(function(a,b){return a - b});
        while(amount[2] != 0){
            amount[2] -= 1;
            amount[1] -= 1;
            seconds += 1;
            amount.sort(function(a,b){return a - b});
        }
        return seconds;  
};