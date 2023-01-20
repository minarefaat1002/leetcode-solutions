class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(i,temp):
            if len(temp) >=2:
                res.add(tuple(temp.copy()))
            if i >= len(nums):
                return
            if not temp or temp[-1] <= nums[i]:
                temp.append(nums[i])
                dfs(i+1,temp)
                temp.pop()
            dfs(i+1,temp)
        dfs(0,[])
        return list(res)