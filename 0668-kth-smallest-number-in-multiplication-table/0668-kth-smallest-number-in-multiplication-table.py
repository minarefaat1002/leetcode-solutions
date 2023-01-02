class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        res = 0
        l = 1
        r = n*m
        while l <= r:
            mid = (l+r)//2
            count = 0
            for i in range(m):
                count += min(mid//(i+1),n)
            if count == k:
                res = mid
                r = mid - 1
            elif count < k:
                l = mid + 1
            else:
                r = mid - 1
                res = mid
        return res