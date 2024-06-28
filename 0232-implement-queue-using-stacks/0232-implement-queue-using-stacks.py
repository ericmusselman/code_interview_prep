class MyQueue:

    def __init__(self):
        self.queue = []
        self.helper = []

    def push(self, x: int) -> None:
        while self.queue:
            self.helper.append(self.queue.pop())
        
        self.queue.append(x)
        
        while self.helper:
            self.queue.append(self.helper.pop())

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return not self.queue


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()