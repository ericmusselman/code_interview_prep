class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        total = 0
        for day in range(1, len(prices)):
            if prices[day] > prices[day-1]:
                total += prices[day] - prices[day-1]
                
        return total
            
    # Time: O(n), Space: O(1)