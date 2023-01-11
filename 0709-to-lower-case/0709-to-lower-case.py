class Solution:
    def toLowerCase(self, s: str) -> str:
        newS = ""
        for char in s:
            newS += chr(ord(char) + 32) if ord(char) - ord('A') >= 0 and ord(char) - ord('A') <=25 else char
        return newS