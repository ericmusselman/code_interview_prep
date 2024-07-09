class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations = sorted(citations)
        n = len(citations)
        
        for i, cite in enumerate(citations):
            if n - i <= cite:
                return n - i
        return 0   
    
    # n:    5
    # cite: 3, 4, 5, 90, 100
    # i:    0, 1, 2,  3,   4
    
    # n:    3
    # cite: 1, 2, 3
    # i:    0, 1, 2
    
    # n:    4
    # cite: 3, 3, 3, 3
    # i:    0, 1, 2, 3
    
    # Time: O(N*long(N)) for sort
    # Space: O(N)