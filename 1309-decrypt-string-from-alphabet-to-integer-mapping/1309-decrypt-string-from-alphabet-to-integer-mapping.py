class Solution:
    def freqAlphabets(self, s: str) -> str:
        s+="12"
        newS = ""
        i = 0
        while i < len(s) -2 :
            if s[i+2] == "#":
                newS += chr(ord('a') + int(s[i:i+2])-1)
                i+=3
            else:
                newS += chr(ord('a')-1+int(s[i]))
                i += 1
        return newS