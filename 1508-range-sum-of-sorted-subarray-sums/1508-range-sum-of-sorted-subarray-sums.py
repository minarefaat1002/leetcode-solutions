class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        mod = 10**9 + 7
        for i in range(len(nums)):
            Sum = 0
            for j in range(i,len(nums)):
                Sum += nums[j]
                Sum = Sum%mod
                arr.append(Sum)
        arr.sort()
        return sum(arr[left-1:right])%mod