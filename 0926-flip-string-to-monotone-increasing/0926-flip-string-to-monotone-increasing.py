class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        leftOnes = 0
        rightZeros = 0
        for n in s:
            if n == "0":
                rightZeros += 1
        flips = len(s)
        for i in range(len(s)):
            flips = min(flips,leftOnes + rightZeros)
            if s[i] == "1":
                leftOnes += 1
            else:
                rightZeros -=1
        return min(flips,leftOnes + rightZeros)