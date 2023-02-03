class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 1
        r = position[-1]
        res = -1
        while l <= r:
            mid = (l+r)//2
            k = m
            k-=1
            i = 1
            left = position[0]
            while i < len(position):
                if position[i] - left>=mid:
                    left = position[i]
                    k-=1
                i+=1
            if k<=0:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res