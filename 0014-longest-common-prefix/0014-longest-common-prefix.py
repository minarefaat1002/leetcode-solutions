class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        iss = False
        for j in range(len(strs[0])):
            for i in range(len(strs)-1):
                if j>=len(strs[i+1]) or strs[i][j]!=strs[i+1][j]:
                    iss = True
                    break
            if iss:
                break
            res+=strs[0][j]
        return res
            