class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] != nums[mid+1] and nums[mid]!= nums[mid-1]:
                return nums[mid]
            elif nums[mid] == nums[mid-1] and mid%2==1:
                l = mid+1
            elif nums[mid] == nums[mid+1] and mid%2==0:
                l = mid+1
            else:
                r = mid - 1