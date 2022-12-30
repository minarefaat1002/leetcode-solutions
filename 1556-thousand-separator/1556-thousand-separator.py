class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return "0"
        i = 0
        s = ""
        while n:
            i+=1
            lastDigit = n%10
            n = n//10
            s = str(lastDigit) + s
            if i%3 == 0 and n:
                s = "." + s
        return s
            
            