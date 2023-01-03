class Solution:
    def countOdds(self, low: int, high: int) -> int:
        1,2,3,4,5,6,7,8,9,10,11
        return (high-low)//2 + (1 if low%2==1 or high%2 ==1 else 0)
