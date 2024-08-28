class Solution:
    def romanToInt(self, s: str) -> int:
        my_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        answer, i = 0, 0
        while i < len(s):
            if i+1 < len(s) and my_map[s[i]] < my_map[s[i+1]]:
                answer += my_map[s[i + 1]] - my_map[s[i]]
                i += 2
            else:
                answer += my_map[s[i]]
                i += 1
        return answer
        
        # Time: O(1), Space: O(1)
        