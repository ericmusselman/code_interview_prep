class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers)-1
        
        while low < high:
            tmp = numbers[low] + numbers[high]
            
            if tmp == target:
                return [low+1, high+1]
            elif tmp < target:
                low += 1
            else:
                high -= 1
        
        # no solution
        return [-1, -1]
    
    # Time: O(n), Space: O(1)