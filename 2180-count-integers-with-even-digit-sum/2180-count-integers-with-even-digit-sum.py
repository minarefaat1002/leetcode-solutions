class Solution:
    def countEven(self, num: int) -> int:
        def digitsSum(num):
            Sum = 0
            while num:
                digit = num%10
                Sum += digit
                num = num//10
            return Sum
        count = 0
        for i in range(1,num+1):
            if digitsSum(i)%2 == 0:
                count += 1
        return count 