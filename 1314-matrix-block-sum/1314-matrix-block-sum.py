class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefixSum = [[0]*(len(mat[0])+1) for _ in range(len(mat)+1)]
        for i in range(1,len(prefixSum)):
            for j in range(1,len(prefixSum[0])):
                prefixSum[i][j] = mat[i-1][j-1] + prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = 0
                mat[i][j] += prefixSum[min(i+k+1,len(mat))][min(j+k+1,len(mat[0]))]
                mat[i][j] -= prefixSum[min(i+k+1,len(mat))][max(j-k,0)]
                mat[i][j] -= prefixSum[max(i-k,0)][min(j+k+1,len(mat[0]))]
                mat[i][j] += prefixSum[max(i-k,0)][max(j-k,0)]
        return mat