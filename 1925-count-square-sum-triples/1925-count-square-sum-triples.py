class Solution:
    def countTriples(self, n: int) -> int:
        counter = 0
        for i in range(1,n+1,1):
            for j in range(1,n+1,1):
                    if sqrt(i*i + j*j) == int(sqrt(i*i + j*j)) and  sqrt(i*i + j*j) <=n:
                        counter +=1
        return counter 
        '''
        counter = 0
        for i in range(1,n+1,1):
            for j in range(1,n+1,1):
                    if sqrt(i*i + j*j) == int(sqrt(i*i + j*j)) and  sqrt(i*i + j*j) <=n:
                        counter +=1
        return counter 
        '''