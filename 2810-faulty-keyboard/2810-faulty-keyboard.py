class Solution:
    def finalString(self, s: str) -> str:
        newString = ""
        for char in s:
            if char == "i":
                newString = newString[::-1]
            else:
                newString += char
        return newString