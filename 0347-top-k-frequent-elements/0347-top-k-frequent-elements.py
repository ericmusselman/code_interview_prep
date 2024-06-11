class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = Counter(nums)
        heap = []
        
        for num, count in counts.items():
            heapq.heappush(heap, (count, num))  # first element is used to make comparisons in the heap
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [item[1] for item in heap]
        