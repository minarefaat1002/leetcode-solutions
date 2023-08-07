/**
 * @param {string[]} names
 * @param {number[]} heights
 * @return {string[]}
 */
var sortPeople = function(names, heights) {
        map = {};
        for (let i = 0; i < names.length; i++) {
            map[heights[i]] = names[i];
        }
        heights.sort(function(a,b){return a-b}).reverse();
        const res = [];
        for (let i = 0; i < names.length; i++) {
            res.push(map[heights[i]]);
        }
        return res;
};