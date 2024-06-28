class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Brute Force
        """
        max_profit = 0
        for buy_day in range(len(prices) - 1):
            for sell_day in range(buy_day + 1, len(prices)):
                p = prices[sell_day] - prices[buy_day]

                if p > max_profit:
                    max_profit = p
                    
        return max_profit
        
        Complexity: Time: O(n^2), Space: O(1)
        """
        
        # find best day to buy so far, and largest difference possible
        max_profit = 0
        min_seen = float("inf")
        
        for i in range(len(prices)):
            if prices[i] < min_seen:
                min_seen = prices[i]
            elif prices[i] - min_seen > max_profit:
                max_profit = prices[i] - min_seen
                
        return max_profit