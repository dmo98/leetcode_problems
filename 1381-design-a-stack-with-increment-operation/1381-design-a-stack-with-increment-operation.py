class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if self.stack == []:
            return -1
        val = self.stack.pop()
        return val

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i == len(self.stack): # index out of bounds
                break
            self.stack[i] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)