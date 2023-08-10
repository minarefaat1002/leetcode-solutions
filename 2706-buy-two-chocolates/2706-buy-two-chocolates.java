class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = 101
        min2 = 101
        for price in prices:
            if price < min1:
                temp = min1
                min1 = price
                min2 = temp
            elif price < min2:
                min2 = price
        remainder = money - (min1+min2)
        return remainder if remainder >= 0 else money