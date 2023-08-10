/**
 * @param {string} s
 * @return {string}
 */
var finalString = function(s) {
        newString = "";
        for(let char of s){
            if(char=='i') newString = newString.split("").reverse().join("");
            else newString += char;
        }
        return newString;
};