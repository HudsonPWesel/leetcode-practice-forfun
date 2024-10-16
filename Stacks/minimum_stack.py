class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minimum = 9999999999
        stack_2 = []

        while len(self.stack) > 0:
            current = self.stack.pop()
            minimum = min(current, minimum)
            stack_2.append(current)
        while len(stack_2) > 0:
            self.stack.append(stack_2.pop())
        return minimum


["MinStack", "push", "push", "push", "top", "pop", "getMin", "pop", "getMin",
    "pop", "push", "top", "getMin", "push", "top", "getMin", "pop", "getMin"]

minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.getMin())
minStack.pop()
minStack.top()
print(minStack.getMin())
