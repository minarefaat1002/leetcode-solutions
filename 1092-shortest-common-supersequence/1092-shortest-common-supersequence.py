class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
        for i in range(len(str1)-1,-1,-1):
            for j in range(len(str2)-1,-1,-1):
                if str1[i] == str2[j]:
                    dp[i][j] = 1+ dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        LCS = ""
        i = 0 
        j = 0
        while dp[i][j] != 0:
            if str1[i] == str2[j]:
                LCS += str1[i]
                i+=1
                j+=1
            else:
                if dp[i+1][j] == dp[i][j]:
                    i+=1
                elif dp[i][j+1] == dp[i][j]:
                    j+=1
        z = 0
        i = 0
        j = 0
        SCS = ""
        while z < len(LCS):
            commonChar = LCS[z]
            while str1[i] != commonChar:
                SCS += str1[i]
                i+=1
            while str2[j] != commonChar:
                SCS += str2[j]
                j+=1
            SCS += commonChar
            i+=1
            j+=1
            z+=1
        while i < len(str1):
            SCS += str1[i]
            i+=1
        while j < len(str2):
            SCS += str2[j]
            j+=1
        return SCS
            