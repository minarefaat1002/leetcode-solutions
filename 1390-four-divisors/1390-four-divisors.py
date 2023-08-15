class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            sq = int(sqrt(num))
            divisors = 0
            Sum = 0
            for i in range(1,sq+1):
                if num%i == 0:
                    divisors += 2 if num/i != sq else 1
                    Sum += i + num//i
            if divisors == 4:
                total +=Sum
        return total 