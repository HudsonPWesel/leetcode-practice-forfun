

class MinStack:
    def __init__(self):
        self.stack = []
        self.stack_2 = []

    def push(self, val: int) -> None:
        minimum = 99999999999
        minimum = min(val, minimum)
        self.stack.append(val)
        self.stack_2.append(minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.stack_2.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_2.pop()


minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.getMin())
minStack.pop()
minStack.top()
print(minStack.getMin())
