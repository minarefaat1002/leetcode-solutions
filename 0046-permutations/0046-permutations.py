class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        temp = []
        res = []
        def dfs(temp):
            if len(temp) == len(nums):
                res.append(temp.copy())
            for i in range(len(nums)):
                if nums[i] not in temp:
                    temp.append(nums[i])
                    dfs(temp)
                    temp.remove(nums[i])
        dfs(temp)
        return res
