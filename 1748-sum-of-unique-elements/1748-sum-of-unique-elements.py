class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        tally = {}
        for num in nums:
            if num not in tally:
                tally[num] = 1
            else:
                tally[num] +=1
        
        total = 0
        for num in tally:
            if tally[num] == 1:
                total += num
        
        return total
    
    # Time: O(n)
    # Space: O(n)
                