class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = []
        for score,age in zip(scores,ages):
            arr.append([age,score])
        arr.sort()
        dp = [score for age,score in arr]
        for i in range(1,len(arr)):
            for j in range(i):
                if arr[i][1] >= arr[j][1]:
                    dp[i] = max(dp[i],dp[j]+arr[i][1])
        return max(dp)