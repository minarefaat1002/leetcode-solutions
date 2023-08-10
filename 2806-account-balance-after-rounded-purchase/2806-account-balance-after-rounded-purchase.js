/**
 * @param {number} purchaseAmount
 * @return {number}
 */
var accountBalanceAfterPurchase = function(purchaseAmount) {
            return 100 - parseInt((purchaseAmount + 5)/10) * 10;
};