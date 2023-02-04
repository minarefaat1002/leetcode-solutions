class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def helper(maxDays):
            count = 0
            bouquets = m
            for flower,day in enumerate(bloomDay):
                if day <= maxDays:
                    count += 1
                else:
                    count = 0
                if count == k:
                    bouquets -= 1
                    count = 0
                if bouquets == 0:
                    return True
            return False
        res = -1 
        left = min(bloomDay)
        right = max(bloomDay)
        while left <= right:
            mid = (left + right)//2
            if helper(mid):
                res = mid 
                right = mid - 1
            else:
                left = mid + 1
        return res 