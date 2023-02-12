class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        index = -1
        for i,num in enumerate(number):
            if i <len(number)-1 and num==digit and num < number[i+1]:
                return number[:i]+number[i+1:]
            elif num ==digit:
                index = i
        return number[:index] + number[index+1:]