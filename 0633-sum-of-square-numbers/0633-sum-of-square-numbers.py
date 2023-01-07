class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):
            b = c - a*a
            sqrtB = sqrt(b)
            if int(sqrtB)*int(sqrtB) == b:
                return True
        return False