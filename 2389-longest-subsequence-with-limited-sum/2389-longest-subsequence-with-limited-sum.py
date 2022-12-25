class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def maxSize(query,nums):
            l = 0 
            res = -1
            r = len(nums)-1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] <= query:
                    res = mid
                    l = mid+1
                else:
                    r = mid-1
            return res + 1
        nums.sort()
        ans = []
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        for query in queries:
            size = maxSize(query,nums)
            ans.append(size)
        return ans
            

        