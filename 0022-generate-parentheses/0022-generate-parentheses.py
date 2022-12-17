class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack =[]
        res = []
        def backtrack(openN,closedN): # we dont need to pass stack or res a parameters as the function is nested  
            
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN<n:
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()
        backtrack(0,0)
        return res
        
        # you can add open if open < n
        # you can add closing if close < open
        # valid IIF open == close  == n 
    ''' we can add close open as long as number of close so far  < open '''