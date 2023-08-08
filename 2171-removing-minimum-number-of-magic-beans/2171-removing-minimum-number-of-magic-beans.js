/**
 * @param {number[]} beans
 * @return {number}
 */
var minimumRemoval = function(beans) {
        let totalBeans = 0;
        for(let b of beans) totalBeans+=b;
        beans.sort(function(a,b){return a-b;})
        let minRemoved = Number.MAX_VALUE;
        for(let i=0;i<beans.length;i++){
            minRemoved = Math.min(minRemoved,totalBeans-(beans.length-i)*beans[i]);
        }
        return minRemoved;
};