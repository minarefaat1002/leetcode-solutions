class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for z in range(j+1,len(nums)):
                    for x in range(z+1,len(nums)):
                        if nums[i]+nums[j]+nums[z]==nums[x]:
                            count+=1
        return count 