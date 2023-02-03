class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotateMat(mat):
            rotatedMat = [[0]*len(mat[0]) for _ in range(len(mat))]
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    rotatedMat[j][len(mat[0])-i-1] = mat[i][j]
            return rotatedMat
        for i in range(4):
            rotatedMat = rotateMat(mat)
            if rotatedMat == target:
                return True
            mat = rotatedMat
        return False