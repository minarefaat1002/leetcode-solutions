class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(temp,i):
            if i <= len(nums):
                res.append(temp.copy())
            if i == len(nums):
                return
            prev = 434
            for j in range(i,len(nums)):
                if nums[j] == prev:
                    continue
                temp.append(nums[j])
                dfs(temp,j+1)
                temp.pop()
                prev = nums[j]
        dfs([],0)
        return res