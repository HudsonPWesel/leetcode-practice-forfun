class MinStack:
    def __init__(self):
        self.stack = []
        self.stack_2 = []

    def push(self, val: int) -> None:
        minimum = 99999999999
        minimum = min(val, self.stack_2[-1] if self.stack_2 else val)
        self.stack.append(val)
        self.stack_2.append(minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.stack_2.pop()

    def top(self) -> int:
        return self.stack[-1]
