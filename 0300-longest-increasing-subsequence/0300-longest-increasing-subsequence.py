class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # to generate all possible subsequence it will be like knapsack problem 2*2*2.....*2 = O(2*n) time complexity 
        lis = [1]*len(nums)
        Max = 1
        # the dynamic solution is O(n^2) time complexity 
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    lis[i]=max(lis[j]+1,lis[i])
            Max = max(lis[i],Max)
        return Max