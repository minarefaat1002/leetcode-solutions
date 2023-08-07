/**
 * @param {string[]} words
 * @param {character} separator
 * @return {string[]}
 */
var splitWordsBySeparator = function(words, separator) {
    const result = [];
    for(word of words){
        for(number of word.split(separator)){
            if(number) result.push(number);
        }
    }
    return result;
};