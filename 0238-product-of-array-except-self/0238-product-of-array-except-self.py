class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post =1
        output=[0] * len(nums)
        i=1
        output[0]=1
        while i<len(nums):
            output[i]=nums[i-1]*output[i-1]
            i+=1
        l=len(nums)-1
        while l>=0:
            output[l]=post*output[l]
            post*=nums[l]
            l-=1
        return output
    '''
res = [1] * len(nums)
        prefix =1
        for i in range(len(nums)):
            res[i] = prefix
            prefix*= nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix*= nums[i]
        return res
    '''