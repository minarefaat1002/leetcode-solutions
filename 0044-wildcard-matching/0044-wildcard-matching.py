class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        newP = ""
        for i,char in enumerate(p):
            if len(newP) !=0 and char =="*" and char == newP[-1]:
                continue
            newP +=char
        dp = {}
        def dfs(i,j):
            if i == len(s) and j==len(newP):
                return True
            if j == len(newP):
                return False
            if (i,j) in dp:
                return dp[(i,j)]
            if i<len(s) and s[i] == newP[j] or newP[j] == "?":
                dp[(i,j)] = dfs(i+1,j+1)
                return dp[(i,j)]
            if newP[j] == "*":
                res = False
                for z in range(i,len(s)+1):
                    res = res or dfs(z,j+1)
                dp[(i,j)] = res
                return dp[(i,j)]
        return dfs(0,0)