class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        maxLen = 0
        pos = 0
        neg = 0
        for num in nums:
            if num == 0:
                pos = 0
                neg = 0
            elif num > 0:
                pos += 1
                neg += 1 if neg != 0 else 0
            else:
                temp = neg
                neg = pos + 1
                pos = temp + 1 if temp != 0 else 0
            maxLen = max(maxLen,pos)
        return maxLen