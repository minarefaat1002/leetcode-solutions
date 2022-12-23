class Solution:
    def getLucky(self, s: str, k: int) -> int:
        zeros = 0
        res = 0
        for letter in s:
            if ord(letter)-ord('a')+1>=10:
                temp =100
            else:
                temp =10
            res= (res*temp) + (ord(letter)-ord('a')+1)
        res = str(res)
        for i in range(k):
            result = 0
            for letter in res:
                result +=int(letter)
            res = str(result)
        return result