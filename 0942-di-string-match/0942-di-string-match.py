class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l = 0
        r = len(s)
        res = []
        for char in s:
            if char == "I":
                res.append(l)
                l+=1
            else:
                res.append(r)
                r-=1
        res.append(r)
        return res