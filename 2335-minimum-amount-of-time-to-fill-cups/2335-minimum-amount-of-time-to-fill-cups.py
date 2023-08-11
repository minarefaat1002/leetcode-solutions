class Solution:
    def fillCups(self, amount: List[int]) -> int:
        seconds = 0
        amount.sort()
        while amount[-1]:
            amount[-1] -= 1
            amount[-2] -= 1
            seconds += 1
            amount.sort()
        return seconds 
    