class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        # def reverse(i):
        #     reverse = 0
        #     while i:
        #         reverse = reverse*10 + i%10
        #         i = i//10
        #     return reverse
        # for i in range(num+1):
        #     Sum=i+reverse(i)
        #     if Sum==num:
        #         return True
        def reverse(i):
            reverse = ""
            for digit in i:
                reverse = digit + reverse
            return int(reverse)
        for i in range(num//2,num+1):
            Sum=i+reverse(str(i))
            if Sum==num:
                return True
        return False