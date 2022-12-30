class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # nums.append(0)
        # nums.insert(0,0)
        # stack = []
        # ans = 0
        # for i in range(len(nums)):
        #     while stack and nums[i] < nums[stack[-1]]:
        #         h = nums[stack.pop()]
        #         w = i - stack[-1] -1
        #         if k <= i-2 and k >= stack[-1]:
        #             ans = max(ans, h * w)
        #     stack.append(i)
        # nums.pop()
        # return ans
        l = r = k
        ans = nums[k]
        Min = nums[k]
        n = len(nums)
        while l>0 or r < n-1:
            if l > 0 and r < n-1:
                if nums[l-1] > nums[r+1]:
                    l-=1
                    Min = min(Min,nums[l])
                else:
                    r+=1
                    Min = min(Min,nums[r])
            elif l > 0:
                l-=1
                Min = min(Min,nums[l])
            else:
                r+=1
                Min = min(Min,nums[r])
            ans = max(ans,Min*(r-l+1))
        return ans
        