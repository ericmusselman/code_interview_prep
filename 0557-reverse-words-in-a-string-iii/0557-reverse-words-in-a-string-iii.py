class Solution:
    def reverseWords(self, s: str) -> str:
        output = ""
        
        i, tmp = 0, 0
        
        for j in range(len(s)):
            if s[j] == " " :
                tmp = j-1
                while tmp >= i:
                    output += s[tmp]
                    tmp -= 1   
                i = j+1
                output += " "
                
            elif j == len(s)-1:
                tmp = j
                while tmp >= i:
                    output += s[tmp]
                    tmp -= 1
                
        return output
    
    # Time: O(n)
    # Space: O(1)
    