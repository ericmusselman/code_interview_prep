class Solution:
    def trap(self, height: List[int]) -> int:
        # empty
        if len(height) == 0:
            return 0
        
        output = 0
        n = len(height)

        left_level, right_level = [0] * n, [0] * n
        
        left_level[0] = height[0]
        for i in range(1, n):
            left_level[i] = max(height[i], left_level[i - 1])
        
        right_level[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_level[i] = max(height[i], right_level[i + 1])
        
        # sum the areas
        for i in range(1, n - 1):
            output += min(left_level[i], right_level[i]) - height[i]

        return output
        
        # O(n) in space and time
        