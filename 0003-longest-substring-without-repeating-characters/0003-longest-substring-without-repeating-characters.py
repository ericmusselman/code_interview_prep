from collections import Counter


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = Counter()
        li = ri = max_length = 0
        
        while ri < len(s):
            char_right = s[ri]
            substring[char_right] += 1
            
            while substring[char_right] > 1:
                char_left = s[li]
                substring[char_left] -= 1
                li += 1
                
            max_length = max(max_length, ri - li + 1)
            ri += 1
        return max_length
        