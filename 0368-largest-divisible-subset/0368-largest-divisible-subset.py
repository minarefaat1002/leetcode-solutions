class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        LDS = [1]*len(nums)
        Max = 1
        pivot = 0
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    LDS[i] = max(LDS[i],LDS[j]+1)
                    if Max < LDS[i]:
                        Max = LDS[i]
                        pivot = i
        prev = nums[pivot]
        Max -= 1
        subset = [prev]
        for i in range(pivot-1,-1,-1):
            if prev % nums[i]== 0 and Max == LDS[i]:
                subset.append(nums[i])
                prev = nums[i]
                Max -=1
        return subset
                