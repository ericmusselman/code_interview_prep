class MyStack(object):

    def __init__(self):
        self._top = None
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        queue = self.queue1 if self.queue1 else self.queue2
        queue.append(x)
        self._top = x
        

    def pop(self):
        """
        :rtype: int
        """
        if self.queue1:
            queue1, queue2 = self.queue1, self.queue2
        else:
            queue2, queue1 = self.queue1, self.queue2
            
        while len(queue1) > 1:
            self._top = queue1.popleft()
            queue2.append(self._top)
        return queue1.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        return self._top
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue1 and not self.queue2
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()