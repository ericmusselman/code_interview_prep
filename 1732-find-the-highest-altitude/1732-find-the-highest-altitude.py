class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high = 0
        curr = 0
        for g in gain:
            curr += g
            high = max(high, curr)
        
        return high
    
    # Time: O(N)
    # Space: O(1)
    