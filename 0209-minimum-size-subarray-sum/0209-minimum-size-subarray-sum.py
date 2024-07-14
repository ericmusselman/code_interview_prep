class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        right = 0
        window_sum = 0
        output = float('inf')

        for right in range(0, len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                output = min(output, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return output if output != float('inf') else 0
    
    # Time: O(n), Space: O(1)