class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        newS = ""
        leftParenthesis = 0
        for char in s:
            if char == "(" and leftParenthesis == 0:
                leftParenthesis += 1
            elif char == "(" and leftParenthesis >= 1:
                newS += char
                leftParenthesis+=1
            elif char == ")" and leftParenthesis == 1:
                leftParenthesis = 0
            else:
                newS += char
                leftParenthesis -= 1
        return newS