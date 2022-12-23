class Solution:
    def secondHighest(self, s: str) -> int:
        digits = [False]*10
        for char in s:
            if ord(char)>=48 and ord(char) <=57:
                digits[int(char)] = True
        i = len(digits)-1
        while i>=0 and not digits[i]:
            i-=1
        i-=1
        while i>=0 and not digits[i]:
            i-=1
        return i if i>=0 else -1