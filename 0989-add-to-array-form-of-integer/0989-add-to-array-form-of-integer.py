class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        newNum = 0
        for digit in num:
            newNum = 10*newNum + digit
        result = newNum + k
        return list(int(digit) for digit in list(str(result)))
