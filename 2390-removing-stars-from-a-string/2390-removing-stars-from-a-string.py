class Solution:
    def removeStars(self, s: str) -> str:
        output = []
        
        for char in s:
            if char != '*':
                output.append(char)
            else:
                output.pop()
        return ''.join(output)
        
    # Time: O(n)
    # Space: O(n)