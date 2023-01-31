class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def dfs(vertex):
            if nums[vertex] < 0:
                return 0
            temp = nums[vertex]
            nums[vertex] = -1
            return 1 + dfs(temp)
            
        result = 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                result = max(dfs(i),result)
        return result