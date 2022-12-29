class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        i = 0
        while i < len(num) and k != 0:
            digit = num[i]
            i+=1
            if not stack and digit == "0":
                continue
            while k!= 0 and stack and stack[-1] > digit:
                stack.pop()
                k-=1
            stack.append(digit)
        for j in range(i,len(num)):
            stack.append(num[j])
        i = 0
        while i<len(stack) and stack[i] == "0":
            i+=1
        return "".join(stack[i:len(stack)-k]) if "".join(stack[i:len(stack)-k]) else "0"