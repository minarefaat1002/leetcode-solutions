class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        Min1 = 101
        Min2 = 101
        for price in prices:
            if price < Min1:
                temp = Min1
                Min1 = price
                Min2 = temp
            elif price < Min2:
                Min2 = price
        remainder = money - (Min1+Min2)
        return remainder if remainder >= 0 else money