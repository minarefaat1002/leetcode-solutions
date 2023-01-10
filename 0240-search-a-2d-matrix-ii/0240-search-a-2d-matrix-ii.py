class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == target:
        #             return True 
        # return False
        
        
        # def exists(row,target):
        #     l = 0 
        #     r = len(row) - 1
        #     while l <= r:
        #         mid = (l+r)//2
        #         if row[mid] == target:
        #             return True
        #         elif row[mid] < target:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     return False
        # for i in range(len(matrix)):
        #     row = matrix[i]
        #     if exists(row,target):
        #         return True
        # return False
        r = 0
        c = len(matrix[0]) - 1
        while r < len(matrix) and c>-1:
            row = matrix
            lastCell = matrix[r][c]
            if lastCell == target:
                return True
            elif target > lastCell:
                r += 1
            else:
                c-=1
        return False