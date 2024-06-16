class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # sliding window
        n = len(haystack)
        m = len(needle)
        
        if n < m:
            return -1
                
        for left in range(0, n-m+1):
            for i in range(m):
                if needle[i] != haystack[left+i]:
                    break
                if i == m-1:
                    return left
        return -1                
        