class Solution:
    def digitCount(self, num: str) -> bool:
        count = [0]*10
        for digit in num:
            count[int(digit)]+=1
        for i,digit in enumerate(num):
            if int(digit) != count[i]:
                return False
        return True