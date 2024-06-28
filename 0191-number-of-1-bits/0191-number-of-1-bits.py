class Solution:
    def hammingWeight(self, n: int) -> int:
        # ..., 8, 4, 2, 1
        binary = "{0:b}".format(n)
        output = 0
        for digit in binary:
            output += int(digit)
            
        return output
        
    # Time: O(1), Space: O(1)
