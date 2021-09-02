class MyCircularQueue:

    def __init__(self, k: int):
        self.front = 0 
        self.rear = -1
        self.queue = [None]*k
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull() is True:
            return False
        self.rear = (self.rear + 1)%(self.capacity)
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty() is True:
            return False
        popped = self.queue[self.front]
        self.front = (self.front + 1)%(self.capacity)
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty() is True:
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty() is True:
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.capacity:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()