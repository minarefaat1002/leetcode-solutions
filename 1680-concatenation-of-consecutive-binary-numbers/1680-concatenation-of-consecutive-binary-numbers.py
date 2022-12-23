class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # cur = 1
        # MOD = 10**9 + 7
        # for i in range(2,n+1):
        #     d = math.floor(log(i,2)+1)
        #     cur = ((cur<<d)%MOD + i)%MOD
        # return cur%MOD
        cur = 1
        size = 1
        MOD = 10**9 + 7
        for i in range(2,n+1):
            if i&(i-1) ==0:
                size+=1
            cur = (cur<<size)%MOD + i
        return cur%MOD