class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in nums:
            if num-1 not in num_set:
                curr = num
                my_len = 1
                while curr + 1 in num_set:
                    curr += 1
                    my_len += 1
                
                max_len = max(max_len, my_len)
        
        return max_len
    
    # O(n) in time and space
        