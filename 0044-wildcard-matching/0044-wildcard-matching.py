class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # solution with preprocessing to group all adjacent starts to one star
        # newP = ""
        # for i,char in enumerate(p):
        #     if len(newP) !=0 and char =="*" and char == newP[-1]:
        #         continue
        #     newP +=char
        # dp = {}
        # def dfs(i,j):
        #     if i == len(s) and j==len(newP):
        #         return True
        #     if j == len(newP):
        #         return False
        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     if i<len(s) and s[i] == newP[j] or newP[j] == "?":
        #         dp[(i,j)] = dfs(i+1,j+1)
        #         return dp[(i,j)]
        #     if newP[j] == "*":
        #         res = False
        #         for z in range(i,len(s)+1):
        #             res = res or dfs(z,j+1)
        #         dp[(i,j)] = res
        #         return dp[(i,j)]
        # return dfs(0,0)
        dp = {}
        def dfs(i,j):
            if i == len(s) and j==len(p):
                return True
            if j == len(p):
                return False
            if (i,j) in dp:
                return dp[(i,j)]
            if i<len(s) and s[i] == p[j] or p[j] == "?":
                dp[(i,j)] = dfs(i+1,j+1)
                return dp[(i,j)]
            if j<len(p)-1 and p[j] == "*" and p[j+1] == "*":
                return dfs(i,j+1)
            if p[j] == "*":
                res = False
                for z in range(i,len(s)+1):
                    res = res or dfs(z,j+1)
                dp[(i,j)] = res
                return dp[(i,j)]
        return dfs(0,0)