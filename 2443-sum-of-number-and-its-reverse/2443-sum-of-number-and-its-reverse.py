class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def reverse(i):
            reverse = 0
            while i:
                reverse = reverse*10 + i%10
                i = i//10
            return reverse
        for i in range(num+1):
            Sum=i+reverse(i)
            if Sum==num:
                return True
        