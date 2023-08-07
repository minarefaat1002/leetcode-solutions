class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = [0]*101
        for num in nums:
            count[num] += 1
        Sum = 0
        for i in range(len(count)):
            if count[i] == 1:
                Sum+=i
        return Sum