class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c :
            return mat
        temp =[]
        newMat = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp.append(mat[i][j])
                if len(temp)==c:
                    newMat.append(temp)
                    temp=[]
        return newMat