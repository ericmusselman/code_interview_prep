class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for char in s:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
        
        for char in t:
            if char in counts:
                counts[char] -= 1
                if counts[char] < 0:
                    return False
            else:
                return False
        
        return (0 == sum([counts[x] for x in counts]))
    
    # Time: O(N+M), Space: O(1)