class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1,1] for _ in range(len(nums))] # longest ===> repetition
        Max = 1
        count = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i][0] == 1 + dp[j][0]:
                        dp[i][1] += dp[j][1]
                    elif dp[i][0] < 1 + dp[j][0]:
                        dp[i][0] = 1 + dp[j][0]
                        dp[i][1] = dp[j][1]
            Max = max(Max,dp[i][0])
        for n in dp:
            if n[0] == Max:
                count += n[1]
        return count