class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        newS = ""
        openB = 0
        for char in s:
            if char == "(":
                newS += char
                openB += 1
            elif char ==")" and openB > 0:
                newS += char
                openB -= 1
            elif char == ")" and openB == 0:
                continue
            else:
                newS += char
        s = newS
        newS = ""
        openB = 0
        for char in s[::-1]:
            if char == ")":
                openB+=1
                newS = char + newS
            elif char =="(" and openB > 0:
                newS = char + newS
                openB -= 1
            elif char =="(" and openB == 0:
                continue
            else:
                newS = char + newS
        return newS