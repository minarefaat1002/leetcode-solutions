class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
#         res = []
#         for i in  range(k,len(nums)-k):
#             isGood = True
#             for j in range(i-k+1,i):
#                 if nums[j] > nums[j-1]:
#                     isGood = False
#             for j in range(i+1,i+k):
#                 if nums[j] >nums[j+1]:
#                     isGood = False
#             if isGood:
#                 res.append(i)
#         return res
# The above solution is a brute force solution which runs in time complexity of O(N*k)
        res = []
        dp1 = [1]*len(nums)
        dp2 = [1]*len(nums)
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                dp1[i] = dp1[i-1] + 1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] <= nums[i+1]:
                dp2[i] = dp2[i+1] + 1
        for i in range(k,len(nums)-k):
            if dp1[i-1] >= k and dp2[i+1] >= k:
                res.append(i)
        return res