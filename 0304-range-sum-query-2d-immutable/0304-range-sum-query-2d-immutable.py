class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.numMatrix = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.numMatrix[i+1][j+1] = matrix[i][j]
        for i in range(1,len(self.numMatrix)):
            for j in range(1,len(self.numMatrix[0])):
                self.numMatrix[i][j] += self.numMatrix[i-1][j] + self.numMatrix[i][j-1]-self.numMatrix[i-1][j-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.numMatrix[row2+1][col2+1] - self.numMatrix[row2+1][col1] - self.numMatrix[row1][col2+1] + self.numMatrix[row1][col1]
                


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)