class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res=""
        z=""
        if len(num1) < len(num2):
            temp = num1
            num1=num2
            num2=temp
        for i in range(len(num1)-len(num2)):
            z+="0"
        num2=z+num2
        carrier = 0
        for j in range(len(num1)-1,-1,-1):
            temp = int(num1[j])+int(num2[j])+carrier
            if temp >9:
                carrier=1
                temp =temp %10
            else:
                carrier = 0
            res= str(temp)+res
        if carrier==1:
            res="1"+res
        return res
            