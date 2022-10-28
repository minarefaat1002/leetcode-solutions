class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for z in range(j+1,len(nums)):
        #             for x in range(z+1,len(nums)):
        #                 if nums[i]+nums[j]+nums[z]==nums[x]:
        #                     count+=1
        # return count 
        # the above solution has time complexity of O(N^4) and it's fine for small inputs 
        res = 0
        l = len(nums)
        count = {}
        count[nums[len(nums)-1] - nums[len(nums)-2]] = 1
        
        for i in range(len(nums) - 3, 0, -1):
            for j in range(i - 1, -1, -1):
                res = res + count.get(nums[j] + nums[i],0)  
            for x in range(len(nums) - 1, i, -1):
                count[nums[x] - nums[i]] =count.get(nums[x] - nums[i],0) + 1
        
        return res
    