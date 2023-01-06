class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        setBits = [0]*32
        for num in nums:
            i = 0
            while i < 32 and num:
                mask = 1
                setBits[i] += mask&num
                num>>=1
                i+=1
        count = 0
        for bit in setBits:
            count += (len(nums)-bit)*bit
        return count 