class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def helper(s,p,Set):
            j = 0
            i = 0
            while i < len(s) and j < len(p):
                if i not in Set and s[i] == p[j]:
                    j+=1
                i+=1
            return j == len(p)
        l = 1
        r = len(removable)
        res = 0
        while l <= r:
            mid = (l+r)//2
            Set = set(removable[:mid])
            if helper(s,p,Set):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res