class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        pos = 0
        res = ""
        def valToPos(val):
            return [val//5,val%5]
        i = j = 0
        while pos < len(target):
            r,c = valToPos(ord(target[pos])-ord('a'))
            if i == r and j == c:
                res+="!"
                pos+=1
            elif j<c and i!=5:
                j+=1
                res+="R"
            elif j>c:
                j-=1
                res+="L"
            elif (r>i and i!=4) or (i==4 and j==0 and r>i):
                i+=1
                res+="D"
            elif r<i :
                i-=1
                res+="U"
        return res