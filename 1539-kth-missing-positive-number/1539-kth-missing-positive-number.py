class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k
        if k > arr[-1] - len(arr):
            return arr[-1] + k - (arr[-1] - len(arr))
        l = 0
        r = len(arr) - 1
        res = -1
        while l <= r:
            mid = (l+r)//2
            if arr[mid] - (mid+1) >= k:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return k-(arr[res-1] - (res)) + arr[res-1]