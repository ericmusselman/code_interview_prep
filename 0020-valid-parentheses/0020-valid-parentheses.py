class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        parentheses_pairs = {
            ")": "(", 
            "}": "{", 
            "]": "["
        }
        
        for p in s:
            if p in parentheses_pairs: # i.e., a key in the dict, which are all closing
                t = stack.pop() if stack else None
                if parentheses_pairs[p] != t:
                    return False
            else:
                stack.append(p)
        return True if len(stack) == 0 else False
                
        