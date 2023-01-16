class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        end = [0]*26
        for char in s:
            end[ord(char)-ord('a')] = (sum(end) + 1)%MOD
        return sum(end)%MOD