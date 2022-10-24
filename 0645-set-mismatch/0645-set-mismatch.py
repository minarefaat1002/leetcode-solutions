class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
#         Sum = 0
#         dictionary = set()
#         repeated = 0
#         for num in nums:
#             if num in dictionary:
#                 repeated = num
#             else:
#                 dictionary.add(num)
#             Sum+=num
#         Sum-=repeated
#         n = len(nums)
#         missing = (n*(n+1))//2 - Sum
#         return [repeated,missing]
        repeated = 0
        Sum = 0
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]<0:
                repeated = abs(nums[i])
            else:
                Sum+=abs(nums[i])
                nums[abs(nums[i])-1] *=-1
        n = len(nums)
        missing = n*(n+1)//2 - Sum
        return [repeated,missing]