/**
 * @param {string} s
 * @return {string}
 */
var removeOuterParentheses = function(s) {
        let newS = "";
        let leftParenthesis = 0;
        for(let i = 0; i<s.length;i++){
            let c = s[i];
            if(c == '(' && leftParenthesis == 0) {
                leftParenthesis += 1;
            } else if(c == '(' && leftParenthesis >= 1) {
                newS += c;
                leftParenthesis += 1;
            } else if(c==')' && leftParenthesis == 1){
                leftParenthesis = 0;
            } else {
                newS += c;
                leftParenthesis -= 1;
            }
        }
        return newS;    
};