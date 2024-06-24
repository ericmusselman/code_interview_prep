class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        seen = defaultdict(int)
        first_add = None
        
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
            
        for num in seen:
            if seen[num] == 1:
                return num
            
    # space: O(n)
    # time: O(n)
    
    # ========================================
                
    # trick to get to O(1) space and O(n) time:
    # a = 0
    #    for i in nums:
    #        a ^= i # XOR bit manipulation
                