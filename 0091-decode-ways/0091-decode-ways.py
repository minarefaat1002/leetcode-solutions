class Solution:
    def numDecodings(self, s: str) -> int:
        prev = 1
        prevprev = 1 
        for i in range(len(s)):
            temp = prev
            if s[i] == "0" and (s[i-1] > "2" or s[i-1] == "0"):
                return 0
            elif s[i] == "0":
                temp = 0
                prev = 0
            if i>0 and s[i-1]=="2" and (ord(s[i]) -ord('0')) in [0,1,2,3,4,5,6]:
                prev += prevprev
            if i>0 and s[i-1] =="1":
                prev += prevprev
            prevprev = temp
        return prev