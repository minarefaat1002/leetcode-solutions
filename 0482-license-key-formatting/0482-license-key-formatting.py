class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        newS = ""
        count=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!="-":
                newS = s[i].upper()+newS
                count+=1
            if count == k:
                newS = "-" + newS
                count = 0
        if newS and newS[0] =="-":
            return newS[1:]
        return newS