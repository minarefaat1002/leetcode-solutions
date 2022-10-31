class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True 
    
                           
        
        
        
        
        
        
        
        '''
        for i in range(len(matrix[0])-1):
            num = matrix[0][i]
            x=0
            z=i
            while x<len(matrix) and z<len(matrix[0]):
                if matrix[x][z] != num:
                       return False
                x+=1 
                z+=1
        for i in range(1,len(matrix)-1):
            num = matrix[i][0]
            x =i
            z = 0
            while x<len(matrix) and  z<len(matrix[0]):
                if matrix[x][z] != num:
                    return False 
                x+=1
                z+=1
        return True
        
        '''