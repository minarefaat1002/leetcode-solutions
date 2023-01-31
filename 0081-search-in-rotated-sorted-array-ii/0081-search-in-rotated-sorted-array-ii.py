class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0 
        high = len(nums)-1
        while low <= high :
            mid = int((low+high)/2)
            if nums[mid] == target :
                return True 
            if nums[high] == nums[low]==nums[mid]:
                low+=1
                high-=1
            elif nums[high]>= nums[mid]: # right half is sorted
                if target > nums[mid] and target <= nums[high]:
                    low = mid+1
                else :
                    high = mid -1
            elif nums[mid]>=nums[low]:  # left half is sorted
                if target >= nums[low] and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            
                # have no idea about the array, but we can exclude nums[start] because nums[start] == nums[mid]
        return False
            