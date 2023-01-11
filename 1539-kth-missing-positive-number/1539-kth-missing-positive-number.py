class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr)
        res = -1
        while l < r:
            mid = (l+r)//2
            if arr[mid] - (mid+1) >= k:
                r = mid 
            else:
                l = mid + 1
        return k+l