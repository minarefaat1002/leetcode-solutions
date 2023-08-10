/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var rowAndMaximumOnes = function(mat) {
        let maxCountOnes = 0;
        let rowNumber = 0;
        for(let i = 0; i < mat.length;i++){
            let count = 0;
            for(let j = 0; j< mat[0].length; j++){
                if(mat[i][j] == 1){
                    count += 1;
                }
            }
            if(count > maxCountOnes){
                maxCountOnes = count;
                rowNumber = i;
            }
        }
        return [rowNumber,maxCountOnes];
};