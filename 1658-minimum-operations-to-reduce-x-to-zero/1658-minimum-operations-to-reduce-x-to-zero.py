class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        Sum = sum(nums)
        diff = Sum - x
        if diff < 0:
            return -1
        curSum = 0
        maxLen = -1
        i = 0
        j = 0
        while j<len(nums):
            if curSum == diff:
                maxLen = max(maxLen,j-i)
                curSum-=nums[i]
                i+=1
            elif curSum < diff:
                curSum += nums[j]
                j+=1
            else:
                curSum -=nums[i]
                i+=1

        while curSum > diff:
            curSum -= nums[i]
            i+=1
        if curSum == diff:
            maxLen = max(maxLen,j-i)
        return len(nums)-maxLen if maxLen != -1 else -1