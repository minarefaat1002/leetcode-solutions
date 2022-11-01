class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            if num != 0:
                hashSet.add(num)
        return len(hashSet)