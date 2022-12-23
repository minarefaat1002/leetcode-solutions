class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        hashMap = {}
        nums.sort()
        for num in nums:
            hashMap[num] = hashMap.get(sqrt(num),0) + 1
        Max = -1
        for item in hashMap:
            if hashMap[item] > Max:
                Max = hashMap[item]
        return Max if Max > 1 else -1