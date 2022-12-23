class Solution:
    def reformatNumber(self, number: str) -> str:
        s = ""
        for num in number:
            if ord(num)-ord("0")>=0 and ord(num)-ord("0")<=9:
                s+=num
        length = len(s)
        newNum = ""
        i=0
        while i < length:
            if i+4 == length:
                newNum += s[i:i+2] + "-" + s[i+2:i+4]
                i+=4
            elif i+2 == length:
                newNum += s[i:i+2]
                i+=2
            else:
                newNum += s[i:i+3] + "-"
                i+=3
        return newNum if newNum[-1] != "-" else newNum[:-1]

