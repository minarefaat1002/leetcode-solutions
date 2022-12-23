class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # for each window we want the chars to match the most frequent character to maximize
        # the opportunity of being chosen
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(maxf,count[s[r]])
            if r-l+1-maxf > k:
                count[s[l]] -= 1
                l+=1
            res = max(res,r-l+1)
        return res
        