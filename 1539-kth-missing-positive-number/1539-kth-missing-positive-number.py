class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k
        if k > arr[-1] - len(arr):
            return k + len(arr)
        l = 0
        r = len(arr) - 1
        res = -1
        while l < r:
            mid = (l+r)//2
            if arr[mid] - (mid+1) >= k:
                r = mid 
            else:
                l = mid + 1
        return k+l