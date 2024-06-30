class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lower_bound = self.findBound(nums, target, True)
        if lower_bound == -1:
            return [-1, -1]
        
        upper_bound = self.findBound(nums, target, False)
        
        return [lower_bound, upper_bound]
        
    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        
        low, high = 0, len(nums)-1
        while low <= high:
            
            middle = (low+high)//2
            
            if nums[middle] == target:
                if isFirst:
                    if middle == low or nums[middle-1] != target:
                        return middle
                    high = middle-1
                else:
                    if middle == high or nums[middle+1] != target:
                        return middle
                    low = middle+1
            elif nums[middle] > target:
                high = middle - 1
            else:
                low = middle + 1
                
        return -1
    
    # Time: O(logN), Space: O(1)