# class Solution:
#     def minimumOperations(self, nums: List[int]) -> int:
#         nums.sort()
#         operations = 0
#         for i in range(0,len(nums)):
#             if nums[i] == 0:
#                 continue
#             if i==0 or nums[i] != nums[i-1]:
#                 operations += 1
#         return operations
# this solution has time complexity of O(nlogn) and space complexity of O(N)
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            if num != 0:
                hashSet.add(num)
        return len(hashSet)
#this solution has time complexity of O(N) and space complexity of O(N)