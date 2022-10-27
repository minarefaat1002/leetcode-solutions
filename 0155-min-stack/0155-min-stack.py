# class MinStack:

#     def __init__(self):
#         self.stack =[]
#         self.minStack =[]

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         self.minStack.append(min(val,self.minStack[-1] if self.minStack else val))

#     def pop(self) -> None:
#         self.stack.pop()
#         self.minStack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.minStack[-1]
# this solution has time complexity of O(1) for each operation and space complexity of O(N)
class MinStack:
    def __init__(self):
        self.stack =[]
        self.Min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.Min = val
        elif val >= self.Min:
            self.stack.append(val)
        else:
            self.stack.append(2*val - self.Min)
            self.Min = val
    def pop(self) -> None:
        if self.stack[-1] >= self.Min:
            self.stack.pop()
        else:
            self.Min = 2*self.Min - self.stack[-1]
            self.stack.pop()
    def top(self) -> int:
        if self.stack[-1] >= self.Min:
            return self.stack[-1]
        else:
            return self.Min

    def getMin(self) -> int:
        return self.Min
# this optimized solution has constant space complexity