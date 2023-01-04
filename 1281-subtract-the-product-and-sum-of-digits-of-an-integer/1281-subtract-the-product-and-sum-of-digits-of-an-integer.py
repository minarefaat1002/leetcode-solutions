class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        def product(num):
            product = 1
            while num:
                product *= (num%10)
                num = num // 10
            return product
        def Sum(num):
            Sum = 0
            while num:
                Sum += (num%10)
                num = num // 10
            return Sum 
        return product(n) - Sum(n)