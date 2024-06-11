class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # use max heap to pop the largest differences
        heap = []
        for val in arr:
            difference = abs(x-val)
            heapq.heappush(heap, (-difference, -val))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return sorted([-item[1] for item in heap])
    