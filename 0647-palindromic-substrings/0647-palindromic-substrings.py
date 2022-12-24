class Solution:
    def countSubstrings(self, s: str) -> int:
    # time complexity is O(n^2)
        res = 0
        for i in range(len(s)):
            res+=self.countpali(s,i,i)
            res+=self.countpali(s,i,i+1)
        return res 
    def countpali(self,s,l,r):
        res = 0
        while l>=0 and r <len(s) and s[l] == s[r]:
            res+=1
            l-=1
            r+=1
        return res 