class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        newS = ""
        stack = []
        leftParenthesis = 0
        for char in s:
            if char == "(":
                stack.append(char)
                leftParenthesis+=1
            elif char == ")" and leftParenthesis == 1:
                leftParenthesis = 0
                newS += "".join(stack[1:])
                stack = []
            else:
                stack.append(char)
                leftParenthesis -= 1
        return newS