class MinStack:

    def __init__(self):
        self.stack = []
        self.aux = []
        self.min_so_far = 0

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min_so_far = val
            self.stack.append(val)
            self.aux.append(self.min_so_far)

        else:
            self.min_so_far = min(val, self.aux[-1])
            self.stack.append(val)
            self.aux.append(self.min_so_far)

    def pop(self) -> None:
        self.stack.pop()
        self.aux.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.aux[-1]
        
