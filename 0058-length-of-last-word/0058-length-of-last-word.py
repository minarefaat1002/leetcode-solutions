class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                while i>=0 and s[i]!=" ":
                    count+=1
                    i-=1
                return count
    '''
    another solution
i,length = len(s)-1 , 0
        while s[i] ==" ":
            i-=1
        while i>=0 and s[i] !=" ":
            length +=1
            i-=1
        return length
        
    '''