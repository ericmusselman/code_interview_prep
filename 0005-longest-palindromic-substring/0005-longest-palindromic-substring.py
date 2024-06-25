class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        ans = [0, 0] # initialize answer, assuming at least get a character from input
        
        # all strings length 1 are palindrome
        for i in range(n):
            dp[i][i] = True
        
        # all strings length 2 are palindromes IF the characters are the same
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i, i+1]
        
        # diff = j-i, so j = i+diff
        # diff 2 indicates length 3, diff 3 indicates length 4, ...
        for diff in range(2, n):
            for i in range(n-diff):
                j = i+diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = [i, j]
        
        i, j = ans
        return s[i:j+1]
    