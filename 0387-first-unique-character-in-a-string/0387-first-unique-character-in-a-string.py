class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}
        for i, char in enumerate(s):
            if char in map:
                map[char] = -1
            else:
                map[char] = i
        
        ans = []
        for char in map:
            if map[char] != -1:
                ans.append(map[char])
        return -1 if len(ans) == 0 else min(ans)
        