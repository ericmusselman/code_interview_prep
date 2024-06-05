class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # EVEN: XX-XX
        # ODD:  XXxXX
        
        s = s.lower()
        s = s.replace(" ", "")
        s = ''.join(c for c in s if c.isalnum()) # OR filter(lambda ch: ch.isalnum(), s)
        
        mp = len(s)//2
        
        if len(s) % 2: # odd
            r = mp+1
            l = mp-1
        else: # even
            r = mp
            l = mp-1
            
        for i in range(mp):
            if s[r] != s[l]:
                return False
            r += 1
            l -= 1
        return True
            