class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        hashMap = {}
        for i in range(len(nums)):
            if sqrt(nums[i]) not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] = hashMap[sqrt(nums[i])] +1
        Max = -1
        for item in hashMap:
            Max = max(Max,hashMap[item])
        return Max if Max !=1 else -1