class MedianFinder(object):

    def __init__(self):
        self.max_heap = [] # storage of the smaller half of numbers, one more or same number as min_heap
        self.min_heap = [] # storage of the larger half of numbers, one less or same number as max_heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap)) # convert the sign back
        
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return 0.5*(-self.max_heap[0] + self.min_heap[0])  # even number of elements so avg middle two


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()