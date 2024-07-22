class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        output = []
        new_start, new_end = newInterval[0], newInterval[1]
        i = 0
        n = len(intervals)
        
        # no overlap, before merge
        while i < n and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1
        
        # overlap, merging
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        output.append(newInterval)
        
        # no overlap, post merge
        while i < n:
            output.append(intervals[i])
            i += 1
        
        return output
    
    # Time: O(n), Space: O(1)