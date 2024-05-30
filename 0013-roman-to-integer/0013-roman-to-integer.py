class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        output = 0
        i = 0
        length = len(s)
        
        while i < length:
            if i + 1 < length and roman_values[s[i + 1]] > roman_values[s[i]]:
                output += roman_values[s[i + 1]] - roman_values[s[i]]
                i+=2
            else:
                output += roman_values[s[i]]
                i+=1
        return output
            