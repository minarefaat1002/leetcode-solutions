class Solution:
    def isThree(self, n: int) -> bool:
        counter =0
        for i in range(1,n+1):
            if n%i == 0:
                counter +=1
        if counter ==3:
            return True
        return False