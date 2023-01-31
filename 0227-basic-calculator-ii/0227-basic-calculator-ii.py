class Solution:
    def calculate(self, s: str) -> int:
        stack =[]
        currentNumber = 0
        operation = "+"
        for i in range(len(s)):
            letter = s[i]
            if ord(letter)>=48 and ord(letter)<=57:
                currentNumber = currentNumber * 10 +( ord(letter) -ord("0"))
            if letter =="+" or letter =="/" or letter =="*" or letter =="-" or i==len(s)-1: 
                if operation =="-":
                    stack.append(-1*currentNumber)
                elif operation =="+":
                    stack.append(currentNumber)
                elif operation =="*":
                    stackTop = stack[-1]
                    stack.pop()
                    stack.append(stackTop* currentNumber)
                elif operation =="/":
                    stackTop=stack[-1]
                    stack.pop()
                    stack.append(int(stackTop/currentNumber))
                operation = letter
                currentNumber =0
        result = 0
        while stack:
            result += stack[-1]
            stack.pop()
        return result
            
            
