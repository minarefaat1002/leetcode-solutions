class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}
        def dfs(index,points):
            if index in dp:
                return dp[index]
            if index >= len(questions):
                return 0
            dp[index] = max(questions[index][0] + dfs(index+questions[index][1]+1,points+questions[index][1]),dfs(index+1,points))
            return dp[index]
        return dfs(0,0)