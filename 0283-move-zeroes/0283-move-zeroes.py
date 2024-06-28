class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        n_digits = 0
        
        while n_digits < len(nums):
            if nums[i] == 0:
                nums.append(nums.pop(i))
            else:
                i += 1
            n_digits += 1
