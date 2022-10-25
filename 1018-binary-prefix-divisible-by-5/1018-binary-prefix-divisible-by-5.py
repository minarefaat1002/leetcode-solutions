class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        xi = 0
        for i in range(len(nums)):
            xi = xi*2 + nums[i]
            if xi%5==0:
                nums[i]=True
            else:
                nums[i]=False
        return nums