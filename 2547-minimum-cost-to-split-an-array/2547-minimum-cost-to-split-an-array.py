class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        lengthInRange = [[0]*len(nums) for _ in range(len(nums))]
        for i in range(len(nums)):
            hashMap = {}
            repeated = 0
            for j in range(i,len(nums)):
                hashMap[nums[j]] = hashMap.get(nums[j],0) + 1
                if hashMap[nums[j]] == 2:
                    repeated += 2
                elif hashMap[nums[j]] > 2:
                    repeated += 1
                lengthInRange[i][j] = repeated
        dp = [0]*(len(nums))
        dp[0] = k
        for i in range(1,len(nums)):
            Min = lengthInRange[0][i]+k
            for j in range(i):
                Min = min(dp[j] + lengthInRange[j+1][i] + k,Min)
            dp[i] = Min
        return dp[-1]
            