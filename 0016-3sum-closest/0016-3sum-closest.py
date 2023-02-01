class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                if current_sum < target:
                    l+=1
                else:
                    r-=1
                if abs(current_sum-target) < abs(res-target):
                    res = current_sum
        return res
