class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        array = [0]*n
        
        for i in range(n):
            array[(i+k) % n] = nums[i]
            
        nums[:] = array
        
        # O(n) in time and space