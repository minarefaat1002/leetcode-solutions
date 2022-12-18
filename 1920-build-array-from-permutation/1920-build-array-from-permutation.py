class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        Max = max(nums)+1
        for i in range(len(nums)):
            nums[i] = ((nums[nums[i]%Max])%Max)*Max + nums[i]
        for i in range(len(nums)):
            nums[i] = int(nums[i]/Max)
        return nums