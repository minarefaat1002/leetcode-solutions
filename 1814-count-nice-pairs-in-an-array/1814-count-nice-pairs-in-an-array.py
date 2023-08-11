class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        total = 0
        def reverseNumber(number):
            reversedNumber = 0
            while number:
                reversedNumber = reversedNumber * 10 + number % 10
                number = number//10
            return reversedNumber
        for i in range(len(nums)):
            nums[i] = nums[i] - reverseNumber(nums[i])
        c = Counter(nums)
        for key,value in c.items():
            total += value*(value-1)//2
        return total%(10**9+7)