class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = [digit for digit in str(n)]
        stack = []
        for i in range(len(s)-1,-1,-1):
            if not stack or stack[-1][1] <= s[i]:
                stack.append([i,s[i]])
                continue
            while stack and stack[-1][1] > s[i]:
                popped = stack.pop()
            index = popped[0]
            s[index],s[i] = s[i],s[index]
            break
        nextGreater = int("".join(s[:i+1]) + "".join(sorted(s[i+1:])))
        if len(stack) != len(s) and nextGreater <= 2**31 - 1:
            return nextGreater 
        return -1