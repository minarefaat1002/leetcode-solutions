class Solution {
    public int[] rowAndMaximumOnes(int[][] mat) {
        int maxCountOnes = 0;
        int rowNumber = 0;
        for(int i = 0; i < mat.length;i++){
            int count = 0;
            for(int j = 0; j< mat[0].length; j++){
                if(mat[i][j] == 1){
                    count += 1;
                }
            }
            if(count > maxCountOnes){
                maxCountOnes = count;
                rowNumber = i;
            }
        }
        return new int[] {rowNumber,maxCountOnes};
        //         maxCountOnes = 0
        // rowNumber = -1
        // for i in range(len(mat)):
        //     count = 0
        //     for j in range(len(mat[0])):
        //         if mat[i][j] == 1:
        //             count += 1
        //     if count > maxCountOnes:
        //         maxCountOnes = count 
        //         rowNumber = i
        // return [rowNumber ,maxCountOnes]
                
    }
}