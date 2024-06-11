class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # to find max element in O(log n), use max heap
        stones = [-1*x for x in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            largest = abs(heapq.heappop(stones))
            next_largest = abs(heapq.heappop(stones))
            
            if largest != next_largest:
                heapq.heappush(stones, -abs(largest-next_largest))
                
        return -stones[0] if stones else 0
        