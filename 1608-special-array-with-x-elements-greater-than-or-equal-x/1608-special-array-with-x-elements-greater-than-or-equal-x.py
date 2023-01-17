class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = [0]*(1001)
        for num in nums:
            count[num] += 1
        right = 0
        for i in range(len(count)):
            right += count[i]
        for i in range(len(count)):
            if right == i:
                return i
            right -= count[i]
        return -1