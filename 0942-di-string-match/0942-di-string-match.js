/**
 * @param {string} s
 * @return {number[]}
 */
var diStringMatch = function(s) {
        let l = 0;
        let r = s.length;
        let res = [];
        for (let i = 0; i < s.length;i++){
            res[i] = s[i] == 'I' ? l++ : r--;
        }
        res[s.length] = r;
        return res;
};