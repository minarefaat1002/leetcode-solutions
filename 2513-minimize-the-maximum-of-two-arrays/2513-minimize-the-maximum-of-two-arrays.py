class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        left = 1
        right = 10**10
        res = 10**10
        while left <= right:
            mid = (left+right)//2
            notDivisibleBy1 = mid - mid//divisor1
            notDivisibleBy2 = mid - mid//divisor2
            notDivisibleBy1And2 = mid - mid//((divisor1*divisor2)//gcd(divisor1,divisor2))
            if notDivisibleBy1 >= uniqueCnt1 and notDivisibleBy2 >= uniqueCnt2 and notDivisibleBy1And2 >= uniqueCnt1 + uniqueCnt2:
                res = min(mid,res)
                right = mid - 1 
            else:
                left = mid + 1
        return res