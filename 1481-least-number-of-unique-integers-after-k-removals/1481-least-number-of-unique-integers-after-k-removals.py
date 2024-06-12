class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
        val_freq = Counter(arr)
        freq = list(val_freq.values())
        heapq.heapify(freq)
        
        i = 0
        
        while freq:
            # remove least frequent element, to max uniformity
            i += heapq.heappop(freq)
            # if we removed too many elements, add it back
            if i > k:
                return len(freq)+1
        # ran out of integers
        return 0
    
        # time: O(n log(n))
        # space: O(n)
        