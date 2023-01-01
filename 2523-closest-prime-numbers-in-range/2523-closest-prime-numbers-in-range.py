class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        seive = [True]*(right+1)
        if left <2 and right < 2:
            return [-1,-1]
        seive[0] = False
        seive[1] = False
        seive[2] = True
        for i in range(2,int(sqrt(len(seive))+1)):
            if not seive[i]:
                continue
            j = i*2
            inc = 3
            while j < len(seive):
                seive[j] = False
                j=i*inc
                inc+=1
        l = left
        r = left
        Min = float('inf')
        res = [-1,-1]
        while r < right+1:
            if seive[l] and seive[r] and l != r:
                if r - l < Min:
                    Min = r - l
                    res = [l,r]
                l = r
            elif seive[l]:
                r+=1
            else:
                l+=1
                r+=1
        return res