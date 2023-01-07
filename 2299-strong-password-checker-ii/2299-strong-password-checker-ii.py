class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        lowerCase = False
        upperCase = False
        digit = False
        specialChar = False
        for i in range(len(password)):
            prevChar = password[i-1]
            char = password[i]
            if ord(char)-ord('a') <=25 and ord(char)-ord('a') >=0:
                lowerCase = True
            elif ord(char)-ord('A') <=25 and ord(char)-ord('A') >=0:
                upperCase = True
            elif ord(char) - ord('0') <= 9 and ord(char) - ord('0') >= 0:
                digit = True
            elif char in "!@#$%^&*()-+":
                specialChar = True
            if i > 0 and char == prevChar:
                return False
        return len(password) >= 8 and lowerCase and upperCase and digit and specialChar 