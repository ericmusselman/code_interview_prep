class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # trim any spaces on the end
        s = s.rstrip()
        
        # find length of the last word
        words = s.split(" ")
        last_word = words[-1]
        return len(last_word)