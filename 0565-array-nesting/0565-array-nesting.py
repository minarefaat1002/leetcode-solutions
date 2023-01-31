class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False]*len(nums)
        def dfs(vertex):
            if visited[vertex]:
                return 0
            visited[vertex] = True
            return 1 + dfs(nums[vertex])
        result = 0
        for i in range(len(visited)):
            if not visited[i]:
                result = max(dfs(i),result)
        return result