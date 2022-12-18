class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxStraightSum = float('-inf')
        minStraightSum = float('inf')
        curMax = float('-inf')
        arraySum = 0
        tempMaxSum = 0
        tempMinSum = 0
        for i in range(len(nums)):
            arraySum += nums[i]
            tempMaxSum += nums[i]
            if (maxStraightSum < tempMaxSum):
                maxStraightSum = tempMaxSum
            if tempMaxSum < 0:
                tempMaxSum = 0
            tempMinSum += nums[i]
            if (minStraightSum > tempMinSum):
                minStraightSum = tempMinSum
            if tempMinSum > 0:
                tempMinSum = 0
        if arraySum == minStraightSum:
            return maxStraightSum
        return max(maxStraightSum,arraySum-minStraightSum)