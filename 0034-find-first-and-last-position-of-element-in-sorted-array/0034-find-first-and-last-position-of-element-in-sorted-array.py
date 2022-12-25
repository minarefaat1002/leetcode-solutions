class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[-1,-1]
        first = 0
        last = len(nums)-1
        result = -1
        while first <= last:
            mid = int((first+last)/2)
            if nums[mid]==target:
                result = mid 
                last = mid -1
            elif nums[mid]>target:
                last = mid-1
            else:
                first = mid + 1
        res[0] = result
        first = 0
        last = len(nums)-1
        result = -1
        while first <= last:
            mid = int((first+last)/2)
            if nums[mid]==target:
                result = mid 
                first = mid +1
            elif nums[mid]>target:
                last = mid-1
            else:
                first = mid + 1
        res[1]= result
        return res 