class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = [0]*1001
        res = []
        for num in nums:
            for i in num:
                count[i] +=1
        for i,c in enumerate(count):
            if c == len(nums):
                res.append(i)
        return res