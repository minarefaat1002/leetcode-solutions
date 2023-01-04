class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        def productAndSum(num):
            product = 1
            Sum = 0
            while num:
                digit = num % 10
                product *= digit
                Sum += digit
                num = num // 10
            return [product,Sum]
        product,Sum = productAndSum(n)
        return product - Sum