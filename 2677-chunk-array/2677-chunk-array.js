/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    let chunked = [];
    let i = 0;
    while(i<arr.length){
        let temp = [];
        let j = 0;
        while(j<size && i<arr.length) temp[j++] = arr[i++];
        chunked.push(temp);
    }
    return chunked;
};
