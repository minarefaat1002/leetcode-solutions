class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashMap = {0:-1}
        Sum = 0
        Max = 0
        for i in range(len(nums)):
            Sum += 1 if nums[i] == 1 else -1
            if Sum in hashMap:
                Max = max(Max,i-hashMap[Sum])
            else:
                hashMap[Sum] = i
        return Max