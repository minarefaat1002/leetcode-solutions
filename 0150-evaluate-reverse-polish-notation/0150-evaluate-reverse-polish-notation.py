class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in list("*+-/"):
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if token == "*":
                    stack.append(op1*op2)
                elif token == "+":
                    stack.append(op1+op2)
                elif token == "-":
                    stack.append(op1-op2)
                else:
                    stack.append(op1/op2)
            else:
                stack.append(token)
        return int(stack[-1])