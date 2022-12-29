class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return False if n&(n-1) else True