class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def sumOfDigits(num):
            Sum = 0
            while num:
                Sum += num%10
                num = num//10
            return Sum
        addedNumber = 0
        temp = 10
        i=0
        while sumOfDigits(n) > target:
            addedNumber =  (10-n%10)*(temp**i) + addedNumber
            n = n//10 + 1
            i+=1
        return addedNumber