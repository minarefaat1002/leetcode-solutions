class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        openB = 0
        for char in s:
            if char == "(":
                stack.append(char)
                openB += 1
            elif char ==")" and openB > 0:
                stack.append(char)
                openB -= 1
            elif char == ")" and openB == 0:
                continue
            else:
                stack.append(char)
        s = "".join(stack)
        stack = []
        openB = 0
        for char in s[::-1]:
            if char == ")":
                openB+=1
                stack.append(char)
            elif char =="(" and openB > 0:
                stack.append(char)
                openB -= 1
            elif char =="(" and openB == 0:
                continue
            else:
                stack.append(char)
        return "".join(stack[::-1])