class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # newS = ""
        # count=0
        # for i in range(len(s)-1,-1,-1):
        #     if s[i]!="-":
        #         newS = s[i].upper()+newS
        #         count+=1
        #     if count == k:
        #         newS = "-" + newS
        #         count = 0
        # if newS and newS[0] =="-":
        #     return newS[1:]
        # return newS
        stack = []
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]!="-":
                count+=1
                stack.append(s[i])
            if count == k:
                count = 0
                stack.append("-")
        if stack and stack[-1]=="-":
            stack.pop()
        return "".join(stack).upper()[::-1]