class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                top = matrix[i-1][j]
                leftDiagonal = matrix[i-1][j-1] if j>0 else float('inf')
                rightDiagonal = matrix[i-1][j+1] if j< len(matrix[0]) - 1 else float('inf')
                matrix[i][j] = matrix[i][j] + min(top,leftDiagonal,rightDiagonal)
        Min = float('inf')
        for i in range(len(matrix[0])):
            Min = min(Min,matrix[len(matrix)-1][i])
        return Min
