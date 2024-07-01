class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        meeting_ends = []
        
        intervals.sort(key = lambda x: x[0])
        
        heapq.heappush(meeting_ends, intervals[0][1]) # end time of first meeting
        
        for i in intervals[1:]:
            if meeting_ends[0] <= i[0]:
                heapq.heappop(meeting_ends)
                
            heapq.heappush(meeting_ends, i[1])
            
        return len(meeting_ends)
        
        # Time: O(NlogN) ... logN for sort, Space: O(N)
        