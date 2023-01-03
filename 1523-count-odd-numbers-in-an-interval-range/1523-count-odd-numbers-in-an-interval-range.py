class Solution:
    def countOdds(self, low: int, high: int) -> int:
        1,2,3,4,5,6,7,8,9,10,11
        if low%2 == 0 and high%2 == 0:
            return (high-low)//2
        elif low%2 == 1 and high%2 == 1:
            return (high-low)//2 + 1
        else:
            return (high-low+1)//2