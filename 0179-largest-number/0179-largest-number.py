class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,num in enumerate(nums):
            nums[i] = str(num)
        def comparator(num1,num2):
            if num1 + num2 > num2 + num1:
                return -1
            else:
                return 1
        nums = sorted(nums,key = cmp_to_key(comparator))
        return str(int("".join(nums)))