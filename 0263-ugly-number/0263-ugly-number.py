class Solution:
    def isUgly(self, n: int) -> bool:
        while n:
            if n==1:
                return True
            elif n%5==0:
                n=n/5
            elif n%3==0:
                n=n/3
            elif n%2==0:
                n=n/2
            else:
                return False
        # if n<=0:
        #     return False
        # while n!=1:
        #     if fmod(n,2)==0:
        #         n=n/2
        #     elif fmod(n,3) ==0:
        #         n=n/3
        #     elif fmod(n,5) == 0:
        #         n = n/5
        #     else:
        #         return False
        # return True
                
        '''
        another solution 
        if n<=0
            return False
        for p in [2,3,5]:
            while n%p ==0:
                n = n//p        #// for integer division 
        return n==1    #it means if n is equal to one then it will return true 
        '''