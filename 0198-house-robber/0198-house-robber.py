class Solution:
    def rob(self, nums: List[int]) -> int:
        # def dfs(i):
        #     if i == len(nums)-2:
        #         return max(nums[len(nums)-1],nums[len(nums)-2])
        #     elif i == len(nums)-1:
        #         return nums[i]
        #     return max(nums[i]+dfs(i+2),dfs(i+1))
        # return dfs(0)
        # the above solution has time complexity O(2^n) and it's so slow ===> leads to time limit exeeded 
        hashmap = {len(nums)-1:nums[len(nums)-1] , len(nums)-2:max(nums[len(nums)-2],nums[len(nums)-1])}
        def dfs(i):
            if i in hashmap:
                return hashmap[i]
            hashmap[i] = max(nums[i]+dfs(i+2),dfs(i+1))
            return hashmap[i]
        return dfs(0)
        # the above solution has time complexity of O(n) and the space complexity is O(n)
        