class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        from collections import deque
        newS = ""
        queue = deque()
        leftParenthesis = 0
        for char in s:
            if char == "(":
                queue.append(char)
                leftParenthesis+=1
            elif char == ")" and leftParenthesis == 1:
                leftParenthesis = 0
                queue.popleft()
                newS += "".join(queue)
                queue.clear()
            else:
                queue.append(char)
                leftParenthesis -= 1
        return newS