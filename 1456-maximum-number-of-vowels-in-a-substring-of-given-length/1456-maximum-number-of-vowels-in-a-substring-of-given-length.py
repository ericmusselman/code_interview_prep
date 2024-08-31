class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # k = right-left+1
        vowels = ['a', 'e', 'i', 'o', 'u']        
        
        n = 0 # tally vowels, rolling    
        left = 0
        right = k+left-1
        
        for i in range(left, right+1):
            if s[i] in vowels:
                n +=1
        output = n
        
        while right < len(s)-1:
            if s[left] in vowels:
                n -= 1
            
            if s[right+1] in vowels:
                n += 1
            
            left += 1
            right += 1
            
            output = max(output, n)
        
        return output
            
        # grow string until length = k
        # count how many vowels
        
        # add right character, +1 to answer if it is a vowel
        # remove left character, -1 to answer if it is a vowel
        
        # Time: O(N)
        # Space: O(1)
        