class Solution:
    def customSortString(self, order: str, s: str) -> str:
        tally = {}
        output = ""
        for char in s:
            if char not in tally:
                tally[char] = 1
            else:
                tally[char] += 1
        
        for char in order:
            if char in tally:
                count = tally[char]
                for i in range(count):
                    output += char
        
        for char in s:
            if char not in order:
                output += char
        
        return output
    
    # Time:  O(n)
    # Space: O(n)
        