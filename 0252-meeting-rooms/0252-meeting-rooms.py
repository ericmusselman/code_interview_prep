class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        if len(intervals) == 1:
            return True
        
        intervals.sort()
        
        for idx in range(len(intervals)-1):
            if intervals[idx+1][0] < intervals[idx][1]:
                return False
        return True
    
    # Time: O(n*log(n)), Space: O(n)
        
