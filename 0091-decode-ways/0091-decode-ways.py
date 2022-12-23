class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=="0":
            return 0
        if len(s)==1:
            return 1
        val1 = 1
        val2 = 1
        for i in range(1,len(s)):
            d1 = int(s[i])
            d2 = int(s[i-1])*10 + int(s[i])
            val = 0
            if d1 >=1:
                val+=val2
            if d2>=10 and d2<=26:
                val+=val1
            val1 = val2
            val2 = val
        return val2