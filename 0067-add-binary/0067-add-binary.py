class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b)>len(a):
            temp = a
            a=b
            b=temp
        z=""
        carrier = 0
        for i in range(len(a)-len(b)):
            z+="0"
        b = z+b
        res = ""
        for i in range(len(a)-1,-1,-1):
            temp = int(a[i])+int(b[i])+carrier
            if temp ==2:
                carrier =1
                res="0" +res
            elif temp ==3:
                carrier =1 
                res="1" +res
            elif temp==1:
                res="1" + res
                carrier = 0
            elif temp ==0:
                res="0" + res
                carrier = 0
        if carrier==1:
            res = "1"+res
        return res