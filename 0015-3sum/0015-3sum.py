class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        
        for i in range(len(nums)):
            # impossible to sum to 0 because other two values will also be pos.
            if nums[i] > 0:
                break
            
            # check for duplicates, if first value then check if possible (i.e., no previous duplicate)
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSumII(nums, i, output)
                
        return output
            
    def twoSumII(self, nums: List[int], i: int, output: List[List[int]]):
        low, high = i+1, len(nums)-1
        while low < high:
            check_sum = nums[i] + nums[low] + nums[high]
            if check_sum < 0:
                low += 1
            elif check_sum > 0:
                high -= 1
            else:
                # found an answer!
                output.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                
                # deal with duplicates and move to next
                while low < high and nums[low] == nums[low-1]:
                    low += 1
                    
        # Time: O(n)
        # Space: O(1)
        
    # Total Time: O(n^2 + nlogn) = O(n^2), called twoSumII n times
    # Space: O(n)