class Solution:
    def hammingWeight(self, n: int) -> int:
        # res = 0
        # while n:
        #     res += n%10
        #     n = n//10
        # return res
        res = 0
        while n:
            res += n%2
            n = n>>1
        return res