/**
 * @param {number[]} prices
 * @param {number} money
 * @return {number}
 */
var buyChoco = function(prices, money) {
        let min1 = 101;
        let min2 = 101;
        for(let price of prices){
            if (price < min1){
                let temp = min1;
                min1 = price;
                min2 = temp;
            } else if(price < min2){
                min2 = price;
            }
        }
        let remainder = money - (min1+min2);
        return remainder >= 0 ? remainder : money;
};