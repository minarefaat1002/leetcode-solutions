class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxCountOnes = 0
        rowNumber = 0
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    count += 1
            if count > maxCountOnes:
                maxCountOnes = count 
                rowNumber = i
        return [rowNumber ,maxCountOnes]
                