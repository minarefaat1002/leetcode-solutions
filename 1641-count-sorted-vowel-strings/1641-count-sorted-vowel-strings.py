class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[],[1,1,1,1,1]]
        for i in range(2,n+1):
            dp.append([0,0,0,0,0])
            for j in range(0,5):
                for z in range(0,j+1):
                    dp[i][j] += dp[i-1][z]
        return sum(dp[n])
# time complexity if O(n) and space complexity is O(n)