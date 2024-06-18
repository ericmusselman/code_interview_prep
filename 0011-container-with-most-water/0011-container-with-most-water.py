class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two pointers: start on left and right extremes (max width), 
        # and move the pointer with the shorter height at each step.
        # Continue while left < right
        
        # What if the heights left and right are the same?
        
        left, right = 0, len(height)-1
        area = 0
        
        while left < right:
            width = right - left
            area = max(area, width * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return area
        
        # Time: O(n), visit each height once
        # Space: O(1)
        