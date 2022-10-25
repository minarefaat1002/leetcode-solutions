class MyQueue:

    def __init__(self):
        self.stack2 = []
    def push(self, x: int) -> None:
        stack1 = []
        while self.stack2:
            stack1.append(self.stack2.pop())
        self.stack2.append(x)
        while stack1:
            self.stack2.append(stack1.pop())

    def pop(self) -> int:
        return self.stack2.pop()

    def peek(self) -> int:
        return self.stack2[-1]

    def empty(self) -> bool:
        if not self.stack2:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()