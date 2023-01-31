class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(float('-inf'))
        nums.insert(0,float('-inf'))
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = int((r+l)/2)
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid-1
            elif nums[mid+1] > nums[mid]:
                l = mid+1
            elif nums[mid+1] < nums[mid]:
                r = mid-1